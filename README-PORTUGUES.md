# 💸 MoneyPrinterTurbo - Gerador Automático de Vídeos com IA

<div align="center">
<h1 align="center">MoneyPrinterTurbo 💸</h1>

<p align="center">
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/stargazers"><img src="https://img.shields.io/github/stars/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Stargazers"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/issues"><img src="https://img.shields.io/github/issues/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/network/members"><img src="https://img.shields.io/github/forks/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/blob/main/LICENSE"><img src="https://img.shields.io/github/license/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="License"></a>
</p>
<br>
<h3>Português | <a href="README-en.md">English</a> | <a href="README.md">简体中文</a></h3>
</div>

## 🎯 Sobre o Projeto

Apenas forneça um **tema** ou **palavra-chave** de vídeo, e o MoneyPrinterTurbo gerará automaticamente:

- ✅ **Roteiro do vídeo** (com IA)
- ✅ **Materiais de vídeo** (Pexels/Pixabay)
- ✅ **Legendas** (Edge/Whisper)
- ✅ **Música de fundo** (aleatória ou personalizada)
- ✅ **Vídeo final em HD** (9:16 ou 16:9)

## 🚀 Características Principais

- [x] **Interface Web** intuitiva e **API REST** completa
- [x] **Múltiplos provedores de IA**: OpenAI, Gemini, DeepSeek, G4F, etc.
- [x] **Geração em lote** - crie vários vídeos e escolha o melhor
- [x] **Suporte multilíngue** - português, inglês, chinês
- [x] **Vozes realistas** - Azure TTS, SiliconFlow
- [x] **Materiais HD gratuitos** - Pexels, Pixabay
- [x] **Legendas personalizáveis** - fonte, cor, posição

## 📋 Requisitos

- **CPU**: 4+ núcleos
- **RAM**: 4GB+
- **Sistema**: Windows 10+, macOS 11+, Linux
- **Rede**: Conexão estável (para download de materiais)

## ⚡ Início Rápido

### 1. **Google Colab** (Recomendado para teste)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/harry0703/MoneyPrinterTurbo/blob/main/docs/MoneyPrinterTurbo.ipynb)

### 2. **Docker** (Mais fácil)
```bash
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
cd MoneyPrinterTurbo
docker-compose up
```

### 3. **Instalação Local**
```bash
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
cd MoneyPrinterTurbo
pip install -r requirements.txt
python webui/Main.py  # Interface Web
python main.py        # API
```

## 🔑 Configuração de API Keys

### **OBRIGATÓRIAS:**
- **Pexels API**: [Registrar aqui](https://www.pexels.com/api/) (gratuito)

### **OPCIONAIS (escolha uma para IA):**
- **G4F**: Gratuito, sem chave necessária ⭐ **Recomendado**
- **OpenAI**: Pago, [obter chave](https://platform.openai.com/api-keys)
- **DeepSeek**: Pago, [obter chave](https://platform.deepseek.com/api_keys)
- **Gemini**: Pago, [obter chave](https://makersuite.google.com/app/apikey)

### **Configuração no config.toml:**
```toml
[app]
# Obrigatória
pexels_api_keys = ["sua_chave_pexels_aqui"]

# IA (escolha uma)
llm_provider = "g4f"  # Gratuito
# llm_provider = "openai"  # Pago
# openai_api_key = "sua_chave_openai"
```

## 🎬 Demonstrações

### Retrato 9:16 (TikTok/Instagram)
- **Tema**: "Como aumentar o prazer da vida"
- **Duração**: 30-60 segundos
- **Resolução**: 1080x1920

### Paisagem 16:9 (YouTube)
- **Tema**: "Qual é o significado da vida"
- **Duração**: 1-3 minutos
- **Resolução**: 1920x1080

## 🛠️ Uso

### Interface Web
1. Acesse `http://localhost:8501`
2. Configure suas API keys
3. Digite o tema do vídeo
4. Clique em "Gerar Vídeo"
5. Aguarde o processamento
6. Baixe o vídeo final

### API REST
```bash
curl -X POST "http://localhost:8080/api/v1/video/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "video_subject": "Como fazer exercícios",
    "video_script": "Exercícios são importantes para a saúde...",
    "video_terms": "exercício, saúde, fitness",
    "video_aspect": "portrait"
  }'
```

## 📊 Custos Estimados

### **Gratuito** (Recomendado para começar)
- Pexels: 200 requests/hora
- G4F: Ilimitado
- **Total**: $0/mês

### **Pago** (Para produção)
- Pexels Pro: $10/mês
- OpenAI: $5-20/mês
- **Total**: $15-30/mês

## 🆘 Problemas Comuns

### "No ffmpeg exe could be found"
```bash
# Windows: Baixe de https://www.gyan.dev/ffmpeg/builds/
# Linux/Mac: 
sudo apt install ffmpeg  # Ubuntu
brew install ffmpeg      # macOS
```

### "Rate limit exceeded"
- Aguarde 1 hora (Pexels gratuito)
- Use múltiplas chaves de API
- Considere upgrade para plano pago

### "Invalid API key"
- Verifique se a chave está correta
- Teste a chave individualmente
- Verifique se a conta está ativa

## 📞 Suporte

- **GitHub Issues**: [Reportar problema](https://github.com/harry0703/MoneyPrinterTurbo/issues)
- **Discord**: [Comunidade](https://harryai.cc)
- **Documentação**: [Wiki do projeto](https://github.com/harry0703/MoneyPrinterTurbo/wiki)

## 📝 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## ⭐ Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

---

**MoneyPrinterTurbo** - Transforme ideias em vídeos profissionais com IA! 🚀
