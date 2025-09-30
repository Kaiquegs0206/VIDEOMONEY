# MoneyPrinterTurbo - Gerador de Vídeos com IA

## 🚀 Deploy na Vercel

### Pré-requisitos

1. **Conta na Vercel**: [https://vercel.com](https://vercel.com)
2. **Chaves de API necessárias** (veja seção abaixo)

### Chaves de API Necessárias

#### 🔑 **OBRIGATÓRIAS:**

1. **Pexels API Key** (para vídeos gratuitos)
   - Registre-se em: https://www.pexels.com/api/
   - Plano gratuito: 200 requests/hora
   - Plano pago: até 10.000 requests/hora

#### 🔑 **OPCIONAIS (escolha uma):**

2. **Provedor de IA (LLM):**
   
   **Opção 1 - G4F (GRATUITO):**
   - Não precisa de chave API
   - Configuração: `llm_provider = "g4f"`
   
   **Opção 2 - OpenAI (PAGO):**
   - Registre-se em: https://platform.openai.com/api-keys
   - Configuração: `llm_provider = "openai"`
   - Adicione: `openai_api_key = "sua_chave_aqui"`
   
   **Opção 3 - Google Gemini (PAGO):**
   - Registre-se em: https://makersuite.google.com/app/apikey
   - Configuração: `llm_provider = "gemini"`
   - Adicione: `gemini_api_key = "sua_chave_aqui"`
   
   **Opção 4 - Qwen/Alibaba (PAGO):**
   - Registre-se em: https://dashscope.console.aliyun.com/apiKey
   - Configuração: `llm_provider = "qwen"`
   - Adicione: `qwen_api_key = "sua_chave_aqui"`

#### 🔑 **OPCIONAIS (para funcionalidades extras):**

3. **Pixabay API Key** (vídeos alternativos)
   - Registre-se em: https://pixabay.com/api/docs/
   - Plano gratuito: 5.000 requests/hora

4. **Azure Speech** (vozes mais realistas)
   - Registre-se em: https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/SpeechServices
   - Adicione: `speech_key` e `speech_region`

### 📋 Passos para Deploy

1. **Fork do repositório** no GitHub
2. **Configure as variáveis de ambiente** na Vercel:
   ```
   PEXELS_API_KEY=sua_chave_pexels
   LLM_PROVIDER=g4f
   G4F_MODEL_NAME=gpt-4o-mini
   ```
3. **Deploy automático** - a Vercel detectará o `vercel.json`
4. **Acesse sua aplicação** no domínio fornecido

### ⚙️ Configuração das Variáveis de Ambiente

Na Vercel, adicione estas variáveis:

```bash
# Obrigatória
PEXELS_API_KEY=sua_chave_pexels_aqui

# Provedor LLM (escolha uma)
LLM_PROVIDER=g4f
# OU
LLM_PROVIDER=openai
OPENAI_API_KEY=sua_chave_openai_aqui
# OU
LLM_PROVIDER=gemini
GEMINI_API_KEY=sua_chave_gemini_aqui

# Opcionais
PIXABAY_API_KEY=sua_chave_pixabay_aqui
SPEECH_KEY=sua_chave_azure_speech_aqui
SPEECH_REGION=sua_regiao_azure_aqui
```

### 🎯 Funcionalidades

- ✅ Geração automática de roteiros
- ✅ Busca de vídeos no Pexels/Pixabay
- ✅ Síntese de voz (Edge TTS gratuito)
- ✅ Geração de legendas
- ✅ Música de fundo
- ✅ Interface web em português
- ✅ API REST completa

### 💡 Dicas de Uso

1. **Para começar**: Use G4F (gratuito) + Pexels
2. **Para produção**: Considere OpenAI + Pexels pago
3. **Para voz realista**: Adicione Azure Speech
4. **Para mais vídeos**: Adicione Pixabay

### 🆘 Suporte

- Discord: https://harryai.cc
- GitHub Issues: [Link do repositório]
- Documentação: [Link da documentação]

### 📄 Licença

MIT License - veja arquivo LICENSE para detalhes.
