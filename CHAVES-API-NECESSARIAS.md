# 🔑 Chaves de API Necessárias - MoneyPrinterTurbo

## 📋 Resumo das Chaves

### 🔴 **OBRIGATÓRIAS (mínimo para funcionar)**

| Chave | Obrigatória | Gratuita | Uso | Link |
|-------|-------------|---------|-----|------|
| **Pexels API** | ✅ SIM | ✅ SIM | Buscar vídeos | https://www.pexels.com/api/ |

### 🟡 **OPCIONAIS (escolha UMA para IA)**

| Chave | Obrigatória | Gratuita | Uso | Link |
|-------|-------------|---------|-----|------|
| **G4F** | ❌ NÃO | ✅ SIM | IA gratuita | Não precisa de chave |
| **OpenAI** | ❌ NÃO | ❌ PAGO | IA paga | https://platform.openai.com/api-keys |
| **Google Gemini** | ❌ NÃO | ❌ PAGO | IA paga | https://makersuite.google.com/app/apikey |
| **Qwen/Alibaba** | ❌ NÃO | ❌ PAGO | IA paga | https://dashscope.console.aliyun.com/apiKey |
| **DeepSeek** | ❌ NÃO | ❌ PAGO | IA paga | https://platform.deepseek.com/api_keys |

### 🟢 **OPCIONAIS (funcionalidades extras)**

| Chave | Obrigatória | Gratuita | Uso | Link |
|-------|-------------|---------|-----|------|
| **Pixabay API** | ❌ NÃO | ✅ SIM | Vídeos alternativos | https://pixabay.com/api/docs/ |
| **Azure Speech** | ❌ NÃO | ❌ PAGO | Vozes realistas | https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/SpeechServices |
| **SiliconFlow** | ❌ NÃO | ❌ PAGO | TTS alternativo | https://siliconflow.cn |

## 🚀 Configurações Recomendadas

### 💰 **Para Começar (GRATUITO)**
```bash
# Obrigatória
PEXELS_API_KEY=sua_chave_pexels

# IA gratuita
LLM_PROVIDER=g4f
G4F_MODEL_NAME=gpt-4o-mini
```

### 💎 **Para Produção (PAGO)**
```bash
# Obrigatória
PEXELS_API_KEY=sua_chave_pexels

# IA paga (escolha uma)
LLM_PROVIDER=openai
OPENAI_API_KEY=sua_chave_openai
OPENAI_MODEL_NAME=gpt-4o-mini

# OU
LLM_PROVIDER=gemini
GEMINI_API_KEY=sua_chave_gemini
GEMINI_MODEL_NAME=gemini-1.0-pro

# Opcionais
PIXABAY_API_KEY=sua_chave_pixabay
SPEECH_KEY=sua_chave_azure_speech
SPEECH_REGION=sua_regiao_azure
```

## 📊 Comparação de Custos

### 💵 **Custos Mensais Estimados**

| Serviço | Plano Gratuito | Plano Pago | Limite Gratuito |
|---------|----------------|------------|-----------------|
| **Pexels** | 200 req/hora | $9.99/mês | 200 req/hora |
| **G4F** | Ilimitado | N/A | Ilimitado |
| **OpenAI** | N/A | $5-50/mês | N/A |
| **Gemini** | N/A | $5-30/mês | N/A |
| **Pixabay** | 5.000 req/hora | $9.99/mês | 5.000 req/hora |
| **Azure Speech** | N/A | $4/milhão chars | N/A |

### 🎯 **Recomendações por Uso**

#### 🆓 **Para Testes/Desenvolvimento:**
- Pexels (gratuito) + G4F (gratuito)
- Custo: **$0/mês**

#### 💼 **Para Uso Pessoal:**
- Pexels (gratuito) + OpenAI ($5/mês)
- Custo: **~$5/mês**

#### 🏢 **Para Produção/Comercial:**
- Pexels pago ($10/mês) + OpenAI ($20/mês) + Azure Speech ($10/mês)
- Custo: **~$40/mês**

## 🔧 Como Obter as Chaves

### 1. **Pexels API Key** (OBRIGATÓRIA)
1. Acesse: https://www.pexels.com/api/
2. Clique em "Get Started"
3. Crie uma conta gratuita
4. Copie sua API Key
5. **Limite**: 200 requests/hora (gratuito)

### 2. **G4F** (GRATUITO - Recomendado)
- Não precisa de chave
- Funciona imediatamente
- **Limite**: Ilimitado

### 3. **OpenAI API Key** (PAGO)
1. Acesse: https://platform.openai.com/api-keys
2. Crie uma conta
3. Adicione créditos ($5 mínimo)
4. Crie uma API Key
5. **Custo**: ~$0.002 por 1K tokens

### 4. **Google Gemini API Key** (PAGO)
1. Acesse: https://makersuite.google.com/app/apikey
2. Faça login com Google
3. Crie uma API Key
4. **Custo**: ~$0.0005 por 1K tokens

### 5. **Pixabay API Key** (OPCIONAL)
1. Acesse: https://pixabay.com/api/docs/
2. Crie uma conta gratuita
3. Copie sua API Key
4. **Limite**: 5.000 requests/hora (gratuito)

### 6. **Azure Speech** (OPCIONAL)
1. Acesse: https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/SpeechServices
2. Crie um recurso de Speech
3. Copie a Key e Region
4. **Custo**: $4 por milhão de caracteres

## ⚙️ Configuração na Vercel

### Variáveis de Ambiente Obrigatórias:
```bash
PEXELS_API_KEY=sua_chave_pexels_aqui
LLM_PROVIDER=g4f
```

### Variáveis de Ambiente Opcionais:
```bash
# Para OpenAI
OPENAI_API_KEY=sua_chave_openai_aqui
OPENAI_MODEL_NAME=gpt-4o-mini

# Para Gemini
GEMINI_API_KEY=sua_chave_gemini_aqui
GEMINI_MODEL_NAME=gemini-1.0-pro

# Para Qwen
QWEN_API_KEY=sua_chave_qwen_aqui
QWEN_MODEL_NAME=qwen-max

# Para DeepSeek
DEEPSEEK_API_KEY=sua_chave_deepseek_aqui
DEEPSEEK_MODEL_NAME=deepseek-chat

# Para Pixabay
PIXABAY_API_KEY=sua_chave_pixabay_aqui

# Para Azure Speech
SPEECH_KEY=sua_chave_azure_speech_aqui
SPEECH_REGION=sua_regiao_azure_aqui

# Para SiliconFlow
SILICONFLOW_API_KEY=sua_chave_siliconflow_aqui
```

## 🧪 Testando as Chaves

### Teste Pexels:
```bash
curl "https://api.pexels.com/videos/search?query=nature&per_page=1" \
  -H "Authorization: SUA_CHAVE_PEXELS"
```

### Teste OpenAI:
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer SUA_CHAVE_OPENAI" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "Hello"}]}'
```

## 🆘 Troubleshooting

### Erro: "No API key provided"
- Verifique se a variável de ambiente está configurada
- Verifique se o nome da variável está correto
- Reinicie o deploy na Vercel

### Erro: "Rate limit exceeded"
- Aguarde 1 hora (Pexels gratuito)
- Considere upgrade para plano pago
- Use múltiplas chaves de API

### Erro: "Invalid API key"
- Verifique se a chave está correta
- Teste a chave individualmente
- Verifique se a conta está ativa

## 📞 Suporte

- **Discord**: https://harryai.cc
- **GitHub Issues**: [Link do repositório]
- **Documentação**: [Link da documentação]
