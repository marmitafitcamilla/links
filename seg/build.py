import json

# Caminhos dos arquivos
CONFIG_FILE = "config.json"
TEMPLATE_FILE = "./templates/template.html"
OUTPUT_FILE = "index.html"

# Carregar JSON
with open(CONFIG_FILE, "r", encoding="utf8") as f:
    config = json.load(f)

# Carregar template HTML
with open(TEMPLATE_FILE, "r", encoding="utf8") as f:
    template = f.read()

# Construir link para WhatsApp
whatsapp_link = f"https://wa.me/{config['phone_number']}?text={config['message'].replace(' ', '%20')}"

# Construir URL completa da imagem (para WhatsApp)
image_full_url = config["url"] + config["image"]

# Substituições
final_html = (
    template
    .replace("{{title}}", config["title"])
    .replace("{{description}}", config["description"])
    .replace("{{image}}", config["image"])
    .replace("{{image_full_url}}", image_full_url)
    .replace("{{url}}", config["url"])
    .replace("{{whatsapp_link}}", whatsapp_link)
    .replace("{{button_text}}", config["button_text"])
    .replace("{{primary_color}}", config["primary_color"])
    .replace("{{redirect_delay}}", str(config["redirect_delay"]))
)

# Gravar arquivo final
with open(OUTPUT_FILE, "w", encoding="utf8") as f:
    f.write(final_html)

print("Arquivo 'index.html' gerado com sucesso!")

