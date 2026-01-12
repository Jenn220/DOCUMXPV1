import os
import re

def clean_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Reemplaza TODOS los patrones de Azure
        # Service Bus
        content = re.sub(
            r'Endpoint=sb://[^;]+;SharedAccessKeyName=[^;]+;SharedAccessKey=[^\s\n]+',
            'Endpoint=sb://YOUR_SERVICEBUS.servicebus.windows.net/;SharedAccessKeyName=YOUR_POLICY;SharedAccessKey=YOUR_KEY_HERE',
            content
        )
        
        # Redis Keys (cualquier base64 largo)
        content = re.sub(
            r'\b[A-Za-z0-9+/]{43,}={0,2}\b',
            'YOUR_REDIS_OR_AZURE_KEY_HERE',
            content
        )
        
        # Storage Account
        content = re.sub(
            r'DefaultEndpointsProtocol=https;AccountName=[^;]+;AccountKey=[^;]+;EndpointSuffix=[^\s\n]+',
            'DefaultEndpointsProtocol=https;AccountName=YOUR_ACCOUNT;AccountKey=YOUR_KEY_HERE;EndpointSuffix=core.windows.net',
            content
        )
        
        # Connection strings genéricas
        content = re.sub(
            r'AccountKey=[A-Za-z0-9+/=]{40,}',
            'AccountKey=YOUR_ACCOUNT_KEY_HERE',
            content
        )
        
        content = re.sub(
            r'SharedAccessKey=[A-Za-z0-9+/=]{40,}',
            'SharedAccessKey=YOUR_SHARED_ACCESS_KEY_HERE',
            content
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"❌ Error en {filepath}: {e}")
        return False

# Limpia todo
count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            if clean_file(filepath):
                count += 1
                print(f"✓ {filepath}")

print(f"\n✅ Archivos limpiados: {count}")