"""Writes the MultiMonitor pages of nowakproduction.github.io (EN + PL)."""
import pathlib, sys

SITE = pathlib.Path(sys.argv[1]) / "multimonitor"
APP = "MultiMonitor"
CONTACT = "https://github.com/nowakproduction/nowakproduction.github.io/issues"
UPDATED_EN, UPDATED_PL = "10 November 2026", "10 listopada 2026"

def page(path, lang, title, current, body, root):
    nav = {
        "en": [("guide", f"{root}", "Guide"), ("privacy", f"{root}privacy/", "Privacy"), ("terms", f"{root}terms/", "Terms"), ("lang", f"{root}pl/", "Polski")],
        "pl": [("guide", f"{root}pl/", "Poradnik"), ("privacy", f"{root}privacy/#pl", "Prywatność"), ("terms", f"{root}terms/#pl", "Regulamin"), ("lang", f"{root}", "English")],
    }[lang]
    links = "".join(f'<a href="{href}"{" aria-current=page" if key == current else ""}>{label}</a>' for key, href, label in nav)
    foot = {"en": f'{APP} is not affiliated with Panasonic. LUMIX is a trademark of Panasonic Holdings Corporation. · <a href="{CONTACT}">Contact</a>',
            "pl": f'{APP} nie jest związana z firmą Panasonic. LUMIX jest znakiem towarowym Panasonic Holdings Corporation. · <a href="{CONTACT}">Kontakt</a>'}[lang]
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body>
<div class="wrap">
<header class="top"><a class="name" href="{root if lang == 'en' else root + 'pl/'}">{APP}</a><nav>{links}</nav></header>
{body}
<footer>{foot}</footer>
</div>
</body>
</html>
"""
    out = SITE / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)

def card(img, title, text, root):
    pic = f'<img src="{root}assets/img/{img}" alt="" loading="lazy">' if img else ""
    return f'<div class="card">{pic}<div class="text"><h3>{title}</h3><p>{text}</p></div></div>'

GUIDE = {
"en": dict(title=f"{APP} — guide", h1="Monitor up to four LUMIX cameras on your iPhone or iPad",
 lead="Live picture from every camera in one grid, recording on all of them with one button, focus peaking, false color, zebra and LUTs — over the cameras' own Wi-Fi, with no internet needed on set.",
 toc=["Getting started", "The camera list", "The grid and REC ALL", "Picture overlays and LUTs", "One camera: focus, exposure, zoom", "Settings", "Free and Multicam", "Cameras", "Troubleshooting", "Coming soon"],
 sections=[
  ("Getting started", """
<p>1. Turn on the camera's Wi-Fi connection to a smartphone (on the camera: <strong>Wi-Fi → connection to a smartphone</strong>).<br>
2. In the app tap <strong>Add camera</strong>. The app looks for the camera by itself: on your phone's personal hotspot, on the camera's own Wi-Fi or on a router you both use.<br>
3. Tap the camera it finds. The first time, iOS asks for access to the <strong>local network</strong> — allow it, the app talks to the cameras over it.<br>
4. Some cameras ask you to confirm the connection on their screen.</p>
<p class="note">A camera takes one controller at a time. Close LUMIX Sync (and any other remote app) before you connect.</p>""", "connect.jpg"),
  ("The camera list", """
<p>Every saved camera has a status: <span class="dot off"></span><strong>offline</strong>, <span class="dot connecting"></span><strong>connecting</strong> and <span class="dot live"></span><strong>connected</strong>.
The link icon connects a camera — even when it moved to another network, the app finds it again. The camera icon opens its picture; the crossed link disconnects it.</p>
<p><strong>Edit</strong> renames cameras, removes them and changes their order — the order of the tiles in the grid. Saved cameras can connect on their own when the app starts.</p>""", None),
  ("The grid and REC ALL", """
<p>All connected cameras side by side. The red button in the middle <strong>starts recording on every camera</strong>. To stop them all, <strong>hold it</strong> — a single tap never stops a take.
A camera that records shows REC and the time on its tile; a red frame marks it.</p>
<p>The app <strong>never stops a recording by itself</strong>: when the link drops, the phone locks or the app goes to the background, the cameras keep recording.</p>
<p>The bar under the grid holds the overlays and four <strong>Fn buttons</strong> you choose yourself. <strong>Display</strong> sets what the tiles show: camera names, frame rate and picture age, function buttons.</p>""", "rec-all.jpg"),
  ("Picture overlays and LUTs", """
<p><strong>Focus peaking</strong> marks the sharp edges, <strong>false color</strong> paints exposure levels, <strong>zebra</strong> stripes the bright areas. Each can be on for all cameras or for some of them (the small 1/4 tag tells how many); colours and thresholds are in the camera settings.</p>
<p>Each camera can show a <strong>LUT</strong> (<code>.cube</code>) applied before the overlays — import your own from the Files app.</p>
<p>The overlays read the camera's live view: a compressed preview of what the camera shows. Use them to judge focus and exposure, not as a measuring instrument.</p>""", "overlays.jpg"),
  ("One camera: focus, exposure, zoom", """
<p>Tap a tile to open the camera full screen. <strong>Tap the picture</strong> to move the focus point there. The pill at the bottom shows aperture, shutter and ISO — tap a value and turn the <strong>dial</strong> to change it.
<strong>Zoom</strong> enlarges the picture 1.5–4× to check focus.</p>""", "focus-exposure.jpg"),
  ("Settings", """
<p>Language (English, Polish), theme (<strong>Dark</strong>, or <strong>Sun</strong> for bright daylight), your licence and restore purchases, help and a diagnostic log you can share when something goes wrong.
The tips above the camera list can be hidden and brought back in <strong>Settings › Help</strong>.</p>""", None),
  ("Free and Multicam", """
<p>One camera is free with every feature. <strong>Multicam</strong> is a one-time purchase that unlocks up to four cameras at once — no subscription. Bought on another device? <strong>Restore purchases</strong> in Settings.</p>""", None),
  ("Cameras", """
<p>Panasonic LUMIX cameras with Wi-Fi remote control. Tested on the LUMIX S5II / S5IIX; other recent LUMIX bodies with the same remote protocol are expected to work.</p>""", None),
  ("Troubleshooting", """
<ul>
<li><strong>The camera is not found</strong> — check that its Wi-Fi connection to a smartphone is on and that LUMIX Sync is closed. On an iPhone hotspot, try turning <strong>Maximize Compatibility</strong> on if the camera cannot see the hotspot.</li>
<li><strong>Nothing connects</strong> — allow Local Network access: iOS Settings › Privacy &amp; Security › Local Network.</li>
<li><strong>REC fails with “busy”</strong> — the camera is in a menu or in playback; close it on the camera.</li>
<li>Still stuck? Tap <strong>Report a problem</strong> in Settings › Help: it opens an e-mail to us with the app version and the latest lines of the diagnostic log. You can also <a href="{CONTACT}">contact us</a> here.</li>
</ul>""", None),
  ("Coming soon", """
<p>Switching AF / MF, AF mode and area, white balance presets, camera status (card time, battery) and focus frames from the camera.</p>""", None),
 ]),
"pl": dict(title=f"{APP} — poradnik", h1="Podgląd do czterech kamer LUMIX na iPhonie i iPadzie",
 lead="Obraz ze wszystkich kamer w jednej siatce, nagrywanie na wszystkich jednym przyciskiem, focus peaking, false color, zebra i LUT-y — przez Wi-Fi kamer, bez internetu na planie.",
 toc=["Pierwsze kroki", "Lista kamer", "Siatka i REC ALL", "Nakładki i LUT-y", "Jedna kamera: ostrość, ekspozycja, powiększenie", "Ustawienia", "Wersja darmowa i Multicam", "Aparaty", "Gdy coś nie działa", "Wkrótce"],
 sections=[
  ("Pierwsze kroki", """
<p>1. Włącz w aparacie połączenie Wi-Fi ze smartfonem (w aparacie: <strong>Wi-Fi → połączenie ze smartfonem</strong>).<br>
2. W aplikacji stuknij <strong>Dodaj kamerę</strong>. Aplikacja sama szuka aparatu: na hotspocie telefonu, w Wi-Fi aparatu albo w routerze, do którego oba są podłączone.<br>
3. Stuknij znaleziony aparat. Za pierwszym razem iOS zapyta o dostęp do <strong>sieci lokalnej</strong> — zezwól, przez nią aplikacja rozmawia z kamerami.<br>
4. Niektóre aparaty proszą o potwierdzenie połączenia na swoim ekranie.</p>
<p class="note">Aparat ma naraz tylko jednego kontrolera. Zamknij LUMIX Sync (i inne aplikacje zdalne), zanim się połączysz.</p>""", "connect.jpg"),
  ("Lista kamer", """
<p>Każda zapisana kamera ma status: <span class="dot off"></span><strong>offline</strong>, <span class="dot connecting"></span><strong>connecting</strong> i <span class="dot live"></span><strong>connected</strong>.
Ikona ogniwa łączy kamerę — nawet gdy zmieniła sieć, aplikacja znajdzie ją ponownie. Ikona kamery otwiera jej obraz, przekreślone ogniwo rozłącza.</p>
<p><strong>Edytuj</strong> zmienia nazwy, usuwa kamery i zmienia ich kolejność — tę samą co kafli w siatce. Zapisane kamery mogą łączyć się same po uruchomieniu aplikacji.</p>""", None),
  ("Siatka i REC ALL", """
<p>Wszystkie połączone kamery obok siebie. Czerwony przycisk na środku <strong>włącza nagrywanie na każdej kamerze</strong>. Żeby zatrzymać wszystkie, <strong>przytrzymaj go</strong> — samo stuknięcie nigdy nie przerwie ujęcia.
Nagrywająca kamera ma na kaflu REC z czasem i czerwoną ramkę.</p>
<p>Aplikacja <strong>nigdy sama nie zatrzymuje nagrania</strong>: przy zerwaniu łącza, zablokowaniu telefonu czy zejściu aplikacji w tło kamery nagrywają dalej.</p>
<p>Pasek pod siatką ma nakładki i cztery <strong>przyciski Fn</strong>, które wybierasz sam. <strong>Display</strong> ustala, co pokazują kafle: nazwy kamer, klatki i wiek obrazu, przyciski funkcyjne.</p>""", "rec-all.jpg"),
  ("Nakładki i LUT-y", """
<p><strong>Focus peaking</strong> zaznacza ostre krawędzie, <strong>false color</strong> koloruje poziomy ekspozycji, <strong>zebra</strong> paskuje jasne miejsca. Każdą włączysz dla wszystkich kamer albo części (mała plakietka 1/4 mówi ilu); kolory i progi są w ustawieniach kamery.</p>
<p>Każda kamera może mieć <strong>LUT</strong> (<code>.cube</code>) nakładany przed nakładkami — własne pliki zaimportujesz z aplikacji Pliki.</p>
<p>Nakładki czytają podgląd z aparatu: skompresowany obraz tego, co pokazuje aparat. Służą do oceny ostrości i ekspozycji, nie do pomiarów.</p>""", "overlays.jpg"),
  ("Jedna kamera: ostrość, ekspozycja, powiększenie", """
<p>Stuknij kafel, aby otworzyć kamerę na całym ekranie. <strong>Stuknij obraz</strong>, aby przenieść tam punkt ostrości. Pigułka na dole pokazuje przysłonę, czas i ISO — stuknij wartość i zmień ją <strong>pokrętłem</strong>.
<strong>Powiększenie</strong> 1,5–4× pomaga sprawdzić ostrość.</p>""", "focus-exposure.jpg"),
  ("Ustawienia", """
<p>Język (polski, angielski), motyw (<strong>Ciemny</strong> albo <strong>Słońce</strong> na jasny dzień), licencja i przywracanie zakupów, pomoc oraz dziennik diagnostyczny do wysłania, gdy coś nie działa.
Wskazówki nad listą kamer ukryjesz i przywrócisz w <strong>Ustawienia › Pomoc</strong>.</p>""", None),
  ("Wersja darmowa i Multicam", """
<p>Jedna kamera jest darmowa, ze wszystkimi funkcjami. <strong>Multicam</strong> to jednorazowy zakup, który odblokowuje do czterech kamer naraz — bez subskrypcji. Kupione na innym urządzeniu? <strong>Przywróć zakupy</strong> w Ustawieniach.</p>""", None),
  ("Aparaty", """
<p>Aparaty Panasonic LUMIX ze zdalnym sterowaniem przez Wi-Fi. Testowane na LUMIX S5II / S5IIX; inne nowe korpusy LUMIX z tym samym protokołem powinny działać.</p>""", None),
  ("Gdy coś nie działa", """
<ul>
<li><strong>Nie widać aparatu</strong> — sprawdź, czy ma włączone połączenie Wi-Fi ze smartfonem i czy LUMIX Sync jest zamknięty. Na hotspocie iPhone'a włącz <strong>Maksymalizuj zgodność</strong>, jeśli aparat nie widzi hotspotu.</li>
<li><strong>Nic się nie łączy</strong> — zezwól na sieć lokalną: Ustawienia iOS › Prywatność i ochrona › Sieć lokalna.</li>
<li><strong>REC kończy się „busy”</strong> — aparat jest w menu albo w odtwarzaniu; zamknij je na aparacie.</li>
<li>Dalej nie działa? Stuknij <strong>Zgłoś problem</strong> w Ustawienia › Pomoc: otworzy się e-mail do nas z wersją aplikacji i ostatnimi wpisami dziennika diagnostycznego. Możesz też <a href="{CONTACT}">napisać do nas</a> tutaj.</li>
</ul>""", None),
  ("Wkrótce", """
<p>Przełączanie AF / MF, tryb i obszar AF, predefiniowany balans bieli, stan aparatu (czas na karcie, bateria) i ramki ostrości z aparatu.</p>""", None),
 ]),
}

def guide(lang, path, root):
    g = GUIDE[lang]
    ids = [f"s{i+1}" for i in range(len(g["sections"]))]
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in zip(ids, g["toc"]))
    parts = [f'<h1>{g["h1"]}</h1><p class="lead">{g["lead"]}</p><div class="toc"><ol>{toc}</ol></div>']
    for i, (title, text, img) in zip(ids, g["sections"]):
        text = text.replace("{CONTACT}", CONTACT)
        pic = f'<div class="card"><img src="{root}assets/img/{img}" alt=""></div>' if img else ""
        parts.append(f'<h2 id="{i}">{title}</h2>{pic}{text}')
    page(path, lang, g["title"], "guide", "\n".join(parts), root)

guide("en", "index.html", "./")
guide("pl", "pl/index.html", "../")

PRIVACY = f"""
<h1>Privacy policy</h1>
<p>Last updated: {UPDATED_EN}</p>
<p>{APP} shows the picture of your cameras and controls them over your local network. We built it to collect as little as possible.</p>
<h3>What stays on your device</h3>
<ul>
<li>Your saved cameras (name, model, network address and identifier), your settings, the LUT files you import and a diagnostic log of what the app did.</li>
<li>The live picture goes straight from the camera to the app and is never stored or sent anywhere.</li>
<li>None of this leaves your device. The diagnostic log is sent only if you choose to share it yourself (for example by e-mail).</li>
</ul>
<h3>What we do not do</h3>
<ul><li>No account, no advertising, no analytics, no tracking, no selling of data.</li></ul>
<h3>Purchases</h3>
<p>Multicam is bought through Apple's App Store; Apple handles the payment. To confirm and restore purchases the app uses <a href="https://www.revenuecat.com/privacy">RevenueCat</a>, which receives an anonymous app user ID and the purchase details from Apple — no name, e-mail or payment card.</p>
<h3>Local network</h3>
<p>iOS asks for access to the local network because the app talks directly to the cameras. The app does not scan the network on its own: it looks for cameras only when you tap Add camera, Connect or Search.</p>
<h3>Children</h3>
<p>The app is not directed at children and does not knowingly collect any data from them.</p>
<h3>Changes and contact</h3>
<p>We will publish changes to this policy on this page. Questions: <a href="{CONTACT}">contact</a>.</p>

<h1 id="pl">Polityka prywatności</h1>
<p>Ostatnia zmiana: {UPDATED_PL}</p>
<p>{APP} pokazuje obraz z Twoich kamer i steruje nimi przez sieć lokalną. Zbiera tak mało, jak się da.</p>
<h3>Co zostaje na urządzeniu</h3>
<ul>
<li>Zapisane kamery (nazwa, model, adres w sieci i identyfikator), ustawienia, zaimportowane pliki LUT i dziennik diagnostyczny działania aplikacji.</li>
<li>Obraz z kamery trafia prosto do aplikacji i nigdzie nie jest zapisywany ani wysyłany.</li>
<li>Nic z tego nie opuszcza urządzenia. Dziennik diagnostyczny wysyłasz tylko sam, jeśli zechcesz (np. e-mailem).</li>
</ul>
<h3>Czego nie robimy</h3>
<ul><li>Bez konta, bez reklam, bez analityki, bez śledzenia, bez sprzedaży danych.</li></ul>
<h3>Zakupy</h3>
<p>Multicam kupujesz przez App Store; płatność obsługuje Apple. Do potwierdzania i przywracania zakupów aplikacja używa usługi <a href="https://www.revenuecat.com/privacy">RevenueCat</a>, która dostaje anonimowy identyfikator aplikacji i dane zakupu od Apple — bez imienia, e-maila ani karty.</p>
<h3>Sieć lokalna</h3>
<p>iOS pyta o dostęp do sieci lokalnej, bo aplikacja łączy się bezpośrednio z kamerami. Aplikacja nie przeszukuje sieci sama z siebie: szuka kamer tylko po stuknięciu Dodaj kamerę, Połącz albo Szukaj.</p>
<h3>Dzieci</h3>
<p>Aplikacja nie jest skierowana do dzieci i świadomie nie zbiera od nich żadnych danych.</p>
<h3>Zmiany i kontakt</h3>
<p>Zmiany tej polityki opublikujemy na tej stronie. Pytania: <a href="{CONTACT}">kontakt</a>.</p>
"""
page("privacy/index.html", "en", f"{APP} — privacy policy", "privacy", PRIVACY, "../")

TERMS = f"""
<h1>Terms of use</h1>
<p>Last updated: {UPDATED_EN}</p>
<p>{APP} is licensed under Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard End User License Agreement</a>. In addition:</p>
<ul>
<li><strong>A monitoring aid.</strong> The app shows a compressed live preview over Wi-Fi. It does not replace checking focus, exposure and recording on the camera itself, and we cannot guarantee that every recording starts or stops — the camera and its card decide.</li>
<li><strong>Multicam</strong> is a one-time, non-consumable in-app purchase. Payments, refunds and restoring go through Apple.</li>
<li><strong>Not affiliated with Panasonic.</strong> LUMIX is a trademark of Panasonic Holdings Corporation; it is used only to name the cameras the app works with.</li>
<li>The app is provided “as is”, to the extent the law allows.</li>
</ul>
<p>Questions: <a href="{CONTACT}">contact</a>.</p>

<h1 id="pl">Regulamin</h1>
<p>Ostatnia zmiana: {UPDATED_PL}</p>
<p>{APP} jest udostępniana na zasadach <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">standardowej licencji użytkownika końcowego Apple</a>. Dodatkowo:</p>
<ul>
<li><strong>Narzędzie pomocnicze.</strong> Aplikacja pokazuje skompresowany podgląd przez Wi-Fi. Nie zastępuje sprawdzenia ostrości, ekspozycji i nagrywania na samym aparacie i nie możemy zagwarantować, że każde nagranie się uruchomi lub zatrzyma — decydują aparat i karta.</li>
<li><strong>Multicam</strong> to jednorazowy zakup w aplikacji. Płatności, zwroty i przywracanie obsługuje Apple.</li>
<li><strong>Brak związku z Panasonic.</strong> LUMIX jest znakiem towarowym Panasonic Holdings Corporation; służy tu tylko do nazwania aparatów, z którymi działa aplikacja.</li>
<li>Aplikacja jest udostępniana „tak jak jest”, w granicach dozwolonych przez prawo.</li>
</ul>
<p>Pytania: <a href="{CONTACT}">kontakt</a>.</p>
"""
page("terms/index.html", "en", f"{APP} — terms of use", "terms", TERMS, "../")
print("ok")
