# 🚀 Guia de Deploy na Vercel

## Passo a Passo Completo

### 1. Preparação do Repositório

1. **Fork do repositório** no GitHub
2. **Clone localmente**:
   ```bash
   git clone https://github.com/SEU_USUARIO/MoneyPrinterTurbo.git
   cd MoneyPrinterTurbo
   ```

### 2. Configuração das Chaves de API

#### 🔑 Chaves OBRIGATÓRIAS:

**Pexels API Key:**
1. Acesse: https://www.pexels.com/api/
2. Crie uma conta gratuita
3. Copie sua API Key
4. Plano gratuito: 200 requests/hora

#### 🔑 Chaves OPCIONAIS:

**Para IA (escolha UMA):**

**Opção A - G4F (GRATUITO):**
- Não precisa de chave
- Configuração: `LLM_PROVIDER=g4f`

**Opção B - OpenAI (PAGO):**
- Acesse: https://platform.openai.com/api-keys
- Crie uma conta e adicione créditos
- Copie sua API Key

**Opção C - Google Gemini (PAGO):**
- Acesse: https://makersuite.google.com/app/apikey
- Crie uma conta
- Copie sua API Key

### 3. Deploy na Vercel

#### Método 1 - Via Vercel CLI:

```bash
# Instalar Vercel CLI
npm i -g vercel

# Login na Vercel
vercel login

# Deploy
vercel --prod
```

#### Método 2 - Via Interface Web:

1. Acesse: https://vercel.com
2. Clique em "New Project"
3. Conecte seu repositório GitHub
4. Configure as variáveis de ambiente
5. Clique em "Deploy"

### 4. Variáveis de Ambiente na Vercel

Adicione estas variáveis no painel da Vercel:

```bash
# OBRIGATÓRIA
PEXELS_API_KEY=sua_chave_pexels_aqui

# Provedor LLM (escolha uma)
LLM_PROVIDER=g4f
G4F_MODEL_NAME=gpt-4o-mini

# OU se usar OpenAI
LLM_PROVIDER=openai
OPENAI_API_KEY=sua_chave_openai_aqui
OPENAI_MODEL_NAME=gpt-4o-mini

# OU se usar Gemini
LLM_PROVIDER=gemini
GEMINI_API_KEY=sua_chave_gemini_aqui
GEMINI_MODEL_NAME=gemini-1.0-pro

# OPCIONAIS
PIXABAY_API_KEY=sua_chave_pixabay_aqui
SPEECH_KEY=sua_chave_azure_speech_aqui
SPEECH_REGION=sua_regiao_azure_aqui
```

### 5. Testando o Deploy

1. **Acesse sua URL** (ex: https://seu-projeto.vercel.app)
2. **Teste a interface web**
3. **Gere um vídeo de teste**
4. **Verifique os logs** na Vercel

### 6. Configurações Avançadas

#### Para Produção:
- Use OpenAI ou Gemini (mais estável)
- Configure Pexels pago (mais requests)
- Adicione Azure Speech (vozes melhores)

#### Para Desenvolvimento:
- Use G4F (gratuito)
- Use Pexels gratuito
- Use Edge TTS (gratuito)

### 7. Monitoramento

- **Logs**: Vercel Dashboard > Functions > Logs
- **Métricas**: Vercel Dashboard > Analytics
- **Erros**: Vercel Dashboard > Functions > Errors

### 8. Troubleshooting

**Erro comum:**
- "No API key provided" → Verifique as variáveis de ambiente
- "Rate limit exceeded" → Aguarde ou use chaves pagas
- "Function timeout" → Aumente o timeout na Vercel

**Soluções:**
1. Verifique todas as variáveis de ambiente
2. Teste as chaves de API individualmente
3. Verifique os logs na Vercel
4. Consulte a documentação da API

### 9. Próximos Passos

Após o deploy bem-sucedido:

1. **Configure domínio personalizado** (opcional)
2. **Configure webhooks** para automação
3. **Monitore o uso** das APIs
4. **Otimize as configurações** conforme necessário

### 10. Suporte

- **Discord**: https://harryai.cc
- **GitHub Issues**: [Link do repositório]
- **Documentação**: [Link da documentação]
