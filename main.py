# Generates WORLD NEWS - 18 NOVEMBER 2026 infographic
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 1100
img = Image.new("RGB", (W, H), "#F5F1E6")
d = ImageDraw.Draw(img)

def font(size, bold=False):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()

d.rectangle([0,0,W,90], fill="#1A2B4A")
d.text((W//2, 45), "WORLD NEWS - 18 NOVEMBER 2026", font=font(42, True), fill="white", anchor="mm")
d.text((W//2, 150), "ESCALATION IN THE GULF", font=font(58, True), fill="#1A2B4A", anchor="mm")
d.text((W//2, 220), "US STRIKES IRANIAN MISSILE SITE AMID RISING TENSIONS", font=font(28, True), fill="#1A2B4A", anchor="mm")

news = [
    ("1. US STRIKES IRAN", "US struck Iranian missile site\non Qeshm Island, Strait of Hormuz."),
    ("2. DIRTY BOMB PROBE", "Trump: US investigating suspected\nIranian dirty bomb plot."),
    ("3. HOUTHIS DRONES", "Houthis launch drones at Saudi\nEast-West oil pipeline. No damage."),
    ("4. IRAQ OIL RESUMES", "Iraq resumes oil via\nKirkuk-Ceyhan to Turkey."),
    ("5. MARKETS", "Brent up, Gold down,\nBTC at $64,647."),
]
x = 40
for title, body in news:
    d.rectangle([x, 300, x+290, 900], outline="#1A2B4A", width=3)
    d.text((x+145, 360), title, font=font(20, True), fill="#1A2B4A", anchor="mm")
    d.text((x+145, 550), body, font=font(18), fill="black", anchor="mm", align="center")
    x += 310

d.rectangle([0,H-60,W,H], fill="#1A2B4A")
d.text((W//2, H-30), "SOURCES: DEFENSE DEPT - SAUDI ENERGY - BAGHDAD - MARKETS DATA", font=font(18), fill="white", anchor="mm")
img.save("output.png")
print("Saved output.png")
