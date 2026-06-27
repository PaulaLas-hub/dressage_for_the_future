import os

OUT = "/home/claude/dressage-site"
os.makedirs(OUT, exist_ok=True)

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=Cinzel:wght@400;600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">'

SHARED_CSS = """<style>
:root{--cream:#F5F0E8;--cream-dark:#EDE7D9;--forest:#1E3A2B;--forest-mid:#2D5040;--forest-light:#3D6B52;--gold:#B8933A;--gold-light:#D4AB55;--gold-pale:#E8D4A0;--ink:#1A1A18;--ink-soft:#3A3830;--mist:#8A8578;}
*{margin:0;padding:0;box-sizing:border-box;}html{scroll-behavior:smooth;}
body{background:var(--cream);color:var(--ink);font-family:'EB Garamond',Georgia,serif;font-size:19px;line-height:1.85;overflow-x:hidden;}
nav{position:fixed;top:0;left:0;right:0;z-index:100;background:var(--forest);display:flex;align-items:center;justify-content:space-between;padding:0 3rem;height:62px;border-bottom:2px solid var(--gold);}
.nav-logo{font-family:'Cormorant Garamond',serif;font-size:1.15rem;font-weight:300;letter-spacing:.06em;color:var(--cream);text-decoration:none;white-space:nowrap;flex-shrink:0;}
.nav-links{display:flex;gap:2rem;list-style:none;align-items:center;margin-left:2rem;}
.nav-links a{font-family:'Cinzel',serif;font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-pale);text-decoration:none;white-space:nowrap;transition:color .3s;}
.nav-links a:hover{color:var(--gold-light);}
.nav-contact{color:var(--gold)!important;border-bottom:1px solid var(--gold);padding-bottom:2px;}
.gold-rule{height:1px;background:linear-gradient(to right,transparent,var(--gold),transparent);}
.article-hero{padding:9rem 8% 4.5rem;background:var(--forest);position:relative;}
.article-hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(to right,transparent,var(--gold),transparent);}
.section-label{font-family:'Cinzel',serif;font-size:.58rem;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);margin-bottom:1.2rem;display:block;}
.article-title{font-family:'Cormorant Garamond',serif;font-size:clamp(2.2rem,5vw,3.8rem);font-weight:300;line-height:1.1;color:var(--cream);max-width:800px;margin-bottom:1rem;}
.article-subtitle{font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-style:italic;color:var(--gold-pale);opacity:.9;max-width:680px;margin-top:.5rem;}
.article-body{max-width:740px;margin:0 auto;padding:5rem 8%;}
.article-body p{margin-bottom:1.6rem;color:var(--ink-soft);}
.article-body h2{font-family:'Cormorant Garamond',serif;font-size:1.9rem;font-weight:300;color:var(--forest);margin:3.5rem 0 1.2rem;line-height:1.2;border-left:2px solid var(--gold);padding-left:1.2rem;}
.article-body h3{font-family:'Cormorant Garamond',serif;font-size:1.35rem;font-weight:400;color:var(--forest);margin:2.5rem 0 .8rem;}
.article-body blockquote{border-left:3px solid var(--gold);padding:1rem 1.5rem;margin:2rem 0;background:var(--cream-dark);font-style:italic;color:var(--ink-soft);}
.article-body ul,.article-body ol{margin:1rem 0 1.6rem 2rem;color:var(--ink-soft);}
.article-body li{margin-bottom:.5rem;}
.article-body a{color:var(--forest);border-bottom:1px solid var(--gold);text-decoration:none;transition:color .3s;}
.article-body a:hover{color:var(--gold);}
.pull-quote{font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-style:italic;font-weight:300;color:var(--forest);border-top:1px solid var(--gold);border-bottom:1px solid var(--gold);padding:2rem 0;margin:3rem 0;line-height:1.5;}
.back-link{display:inline-flex;align-items:center;gap:.6rem;font-family:'Cinzel',serif;font-size:.58rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);text-decoration:none;margin-bottom:2.5rem;border-bottom:1px solid transparent;transition:border-color .3s;}
.back-link:hover{border-bottom-color:var(--gold);}
.next-prev{background:var(--forest);padding:3rem 8%;display:flex;justify-content:space-between;align-items:center;gap:2rem;flex-wrap:wrap;}
.np-item{text-decoration:none;}
.np-label{font-family:'Cinzel',serif;font-size:.5rem;letter-spacing:.2em;text-transform:uppercase;color:var(--mist);display:block;margin-bottom:.4rem;}
.np-title{font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-style:italic;color:var(--gold-pale);display:block;}
.np-item:hover .np-title{color:var(--gold-light);}
.np-right{text-align:right;}
footer{background:var(--ink);padding:3.5rem 8% 2.5rem;}
.footer-inner{display:flex;justify-content:space-between;gap:3rem;flex-wrap:wrap;padding-bottom:2rem;border-bottom:1px solid rgba(184,147,58,.2);margin-bottom:1.5rem;}
.footer-brand h3{font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:var(--cream);margin-bottom:.5rem;}
.footer-brand p{font-size:.9rem;color:var(--mist);max-width:360px;line-height:1.6;}
.footer-nav h4{font-family:'Cinzel',serif;font-size:.55rem;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;margin-bottom:1rem;}
.footer-nav ul{list-style:none;}
.footer-nav li{margin-bottom:.5rem;}
.footer-nav a{font-size:.9rem;color:var(--mist);text-decoration:none;transition:color .3s;}
.footer-nav a:hover{color:var(--gold-pale);}
.footer-bottom{display:flex;justify-content:space-between;font-size:.7rem;color:var(--mist);font-family:'Cinzel',serif;letter-spacing:.1em;opacity:.4;flex-wrap:wrap;gap:.5rem;}
.btn-primary{font-family:'Cinzel',serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;padding:1rem 2.5rem;background:var(--forest);color:var(--gold-pale);text-decoration:none;border:1px solid var(--forest);transition:all .3s;display:inline-block;}
.btn-primary:hover{background:var(--forest-mid);border-color:var(--gold);color:var(--gold-light);}
.btn-secondary{font-family:'Cinzel',serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;padding:1rem 2.5rem;background:transparent;color:var(--forest);text-decoration:none;border:1px solid var(--forest);transition:all .3s;display:inline-block;}
.btn-secondary:hover{background:var(--forest);color:var(--gold-pale);}
.blog-date{font-family:'Cinzel',serif;font-size:.55rem;letter-spacing:.18em;color:var(--mist);text-transform:uppercase;margin-bottom:.5rem;display:block;}
.blog-author{font-family:'Cinzel',serif;font-size:.55rem;letter-spacing:.15em;color:var(--gold);text-transform:uppercase;}
@media(max-width:800px){
  nav{padding:0 1.5rem;}.nav-links{display:none;}
  .article-hero{padding:7rem 6% 3rem;}.article-body{padding:3.5rem 6%;}
  .next-prev{flex-direction:column;gap:1.5rem;}
  .footer-inner{flex-direction:column;}.footer-bottom{flex-direction:column;}
}
</style>"""

NAV = """<nav>
  <a href="index.html" class="nav-logo">Dressage For the Future</a>
  <ul class="nav-links">
    <li><a href="index.html">Home</a></li>
    <li><a href="how-we-got-here.html">How We Got Here</a></li>
    <li><a href="the-future.html">The Future</a></li>
    <li><a href="blog.html">Blog</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="contact.html" class="nav-contact">Contact</a></li>
  </ul>
</nav>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-brand">
      <h3>Dressage for the Future</h3>
      <p>Research, ethics and the future of horse sport.</p>
    </div>
    <div class="footer-nav">
      <h4>Navigate</h4>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="how-we-got-here.html">How We Got Here</a></li>
        <li><a href="the-future.html">The Future</a></li>
        <li><a href="blog.html">Blog</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>&copy; 2026 Dressage for the Future</span>
    <span>Canberra, Australia</span>
  </div>
</footer>"""

def write_page(filename, title, section_label, hero_title, subtitle, body, prev=None, nxt=None):
    np_html = ""
    if prev or nxt:
        p = f'<a href="{prev[0]}" class="np-item"><span class="np-label">&larr; Previous</span><span class="np-title">{prev[1]}</span></a>' if prev else '<span></span>'
        n = f'<a href="{nxt[0]}" class="np-item np-right"><span class="np-label">Next &rarr;</span><span class="np-title">{nxt[1]}</span></a>' if nxt else '<span></span>'
        np_html = f'<div class="next-prev">{p}{n}</div>'
    sub_html = f'<p class="article-subtitle">{subtitle}</p>' if subtitle else ''
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Dressage for the Future</title>
{FONTS}{SHARED_CSS}
</head>
<body>
{NAV}
<div class="article-hero">
  <span class="section-label">{section_label}</span>
  <h1 class="article-title">{hero_title}</h1>
  {sub_html}
</div>
<div class="gold-rule"></div>
<div class="article-body">
  <a href="index.html" class="back-link">&larr; Back to Home</a>
  {body}
</div>
{np_html}
{FOOTER}
</body></html>"""
    with open(f"{OUT}/{filename}", "w") as f:
        f.write(html)
    print(f"✓ {filename}")

# ══════════════════════════════════════════════════════════════════════════════
# PAGES
# ══════════════════════════════════════════════════════════════════════════════

write_page("before-sentience.html",
  "If He Only Had a Brain",
  "How We Got Here",
  "If He Only Had a Brain",
  "How dressage was built on a world that no longer exists.",
  """
<p>In the 18th and 19th century, horses did not have "brains" as we think of them now. They were mechanical beings possessed of weight (mass) and forces.</p>
<p>René Descartes laid this theory down in writing in the 1630s–1640s. The view continued to influence European science through the 17th and into the 18th century. The relevant passages are in Section V of <em>Discourse on Method</em>, and are best understood from his own words:</p>
<blockquote>"And this proves not merely that the beasts have less reason than men, but that they have none at all."</blockquote>
<p>This is the foundation of the "animal-machine" doctrine, which did three powerful things: it justified vivisection, it normalised force-based animal training, and it removed the need to consider animal agency.</p>
<p>This fit beautifully into early modern science because it allowed researchers to study bodies without confronting consciousness. It also fit beautifully into military and agricultural training systems — if the horse is a machine of weight and force, then training is simply the art of applying correct mechanical pressure. No cognition required.</p>
<p>A brute as big as a horse and with strength to match was a prized asset — but only if that power could be harnessed by man. With wars looming and the cavalry being the nuclear weapon of the day, time was tight and the stakes were high.</p>
<h2>Baucher and the Army</h2>
<p>M. Baucher writes in his 1842 book <em>Méthode d'équitation basée sur de nouveaux principes</em>: "The horse, like all organized beings is possessed of a weight and force peculiar to himself." He describes instinctive forces and transmitted forces. The task of the rider was to harness these forces at will — but "the education of the horse consists of the complete subjection of his powers."</p>
<p>Armies had cavalry officers and they all needed horses. There were tens if not hundreds of thousands of horses actively enlisted at the time. Men who could tame these animals and make them submit to their will were highly prized. Men like François Baucher — who had a method that was easy to follow, repeat and duplicate — were revered.</p>
<p>Baucher's training manual for army officers was first published in 1842. It was so popular that in the first year two editions were published, and since then seven more — making nine editions in eight years. After this the French Minister of War decreed that Baucher's method be installed across France, which it was, to enormous success.</p>
<p>His Method of Horsemanship was reprinted in Belgium and translated into Dutch and German. Pupils of his continued his work, and it is still cited today in classical dressage circles. However, context matters — and the context has been forgotten.</p>
  """,
  prev=None,
  nxt=("when-dressage-changed.html", "When Dressage Changed")
)

write_page("when-dressage-changed.html",
  "When Dressage Changed",
  "How We Got Here",
  "When Dressage Changed",
  "Lightness. Self-carriage. Invisible aids — and where they went.",
  """
<p>Dressage did not change overnight. It changed so slowly that almost nobody noticed.</p>
<p>We all know that dressage began with the need to train horses for war. Remember an age before cars? No one really does. It is too far removed from modern life to imagine clearly. Yet for most of human history horses were not a sport or a hobby. They were transport, communication, power, wealth, status, and survival.</p>
<h2>The First Celebrity Trainers</h2>
<p>The great horsemen of earlier centuries were celebrities. They travelled across Europe, performed for royalty, and were hosted in royal courts. When we read their books today something remarkable becomes clear — the scale of their work was incredibly small.</p>
<p>François Baucher, whose theories are still debated today, trained horses from roughly 1820 until his death in 1873. In his entire lifetime he produced twenty-six horses to Haute École — the equivalent of Grand Prix. James Fillis (1834–1913) records that he had produced thirty-five horses. That is the total work of an entire career.</p>
<p>By comparison, Helgstrand Dressage reported approximately 250 horses at its main Danish facility in 2019, and by 2023 controlled around 600 horses across multiple international locations. One is art. The other is production.</p>
<h2>A Conversation Across Centuries</h2>
<p>Many of the great horsemen never actually met one another. François Robichon de la Guérinière (1688–1751), widely considered the father of classical dressage, credited the earlier writings of Salomon de la Broue (1530–1610) — who died seventy-eight years before de la Guérinière was even born. These ideas travelled across generations through imitation, stories, lessons, interpretation, translation, and very few books. Not surprisingly, misunderstandings appeared.</p>
<p>De la Guérinière already showed a deeper sensitivity to equine behaviour: <em>"An understanding of the horse's nature is one of the first basics in the art of riding."</em> He also warned: <em>"No animal better recalls his first improperly applied punishments than the horse."</em></p>
<p>Fillis, writing nearly two centuries later, still expressed doubt: <em>"The great difficulty in breaking is to make the horse understand what we want him to do… because a horse, contrary to what many think, has only a small supply of intelligence."</em></p>
<div class="pull-quote">It is not the horse that lacks intelligence — it is our ability to explain it that has lagged behind.</div>
<h2>The Sentience Problem</h2>
<p>Today we know horses are intelligent animals. More importantly, we recognise that they are sentient — capable of feeling pain, comfort, fear, stress, and pleasure. Although scientists have recognised animal sentience for decades, it was only formally acknowledged in European law in 2009 through the Lisbon Treaty.</p>
<p>Modern dressage is trying to build an ethical framework on top of a historical system that was never designed with animal welfare in mind. This contradiction appears most clearly in debates about whether horses are behind the vertical — but that is only the surface of something much deeper.</p>
<h2>From Art to Industry</h2>
<p>In 1978 the FEI created the Dressage World Cup — a winter indoor circuit designed specifically for spectators. Smaller arenas, brighter lights, louder audiences, more dramatic presentation. All conditions that reward expressive, high-energy movement rather than subtle classical riding. In 1986, the Grand Prix Freestyle to Music was introduced to make dressage more television-friendly. Dressage had become entertainment.</p>
<p>Classical dressage emphasised lightness, balance, self-carriage, and invisible aids. Modern sport dressage increasingly rewards power, expression, maximum movement, and contained energy.</p>
<p>Somewhere between art and industry, something changed. And the horse has been negotiating that change ever since.</p>
<div class="pull-quote">Dressage began as an art. It became a sport. Today it risks becoming an industry.</div>
  """,
  prev=("before-sentience.html", "If He Only Had a Brain"),
  nxt=("her-mouth.html", "Her Mouth, Not Ours")
)

write_page("her-mouth.html",
  "Her Mouth, Not Ours",
  "The Future",
  "Her Mouth, Not Ours",
  "The mouth belongs to the horse.",
  """
<p>The mouth belongs to the horse. It is not sporting equipment. Not a training interface. Not a steering wheel, a balancing aid, or a psychological support system for the rider. It is living tissue. It is sensory. It is neurological. It is how horses explore the world, regulate themselves, connect socially, graze, soothe, and communicate.</p>
<p>Through the mouth they select forage, taste minerals, separate sand from feed, drink, groom, and calm themselves. It is not an accessory attached to the horse. It is part of the nervous system itself.</p>
<p>Placing a bit inside it is therefore not neutral. Applying pressure through it is not neutral. Strapping it shut is not neutral. Controlling an animal's body through one of its most sensitive sensory regions can never be neutral.</p>
<p>Tradition does not make it neutral. Habit does not make it neutral.</p>
<h2>Necessity and Pleasure</h2>
<p>We accept invasive acts when they are necessary. Animals are restrained for medical treatment. Surgery is performed to save life. These are grave compromises justified by survival or welfare. But sport is not necessity. Competition is not necessity. Our hobbies, ambitions, lessons, and beach rides are not necessity. Pleasure does not justify invasion of another body.</p>
<p>For centuries horses were treated as mechanical beings — bodies governed by weight and force rather than minds and agency. Within that worldview domination felt rational. Control could be mistaken for refinement. Compliance could be mistaken for understanding. But that worldview no longer survives serious scientific scrutiny.</p>
<h2>Ownership</h2>
<p>Modern biology and cognitive science recognise horses as intelligent, perceptive, emotionally responsive mammals. They learn through prediction, pattern, and relationship. They possess memory, fear, preference, curiosity, and social awareness. They are not force systems awaiting correction.</p>
<p>This is not a debate about softer hands or gentler contact. It is not about kinder bits or improved technique. It is about ownership. The horse's body belongs to the horse. Yes, in modern law horses remain classified as property. But legality and morality are not the same thing.</p>
<div class="pull-quote">If a discipline requires the invasion of that body in order to function, then the problem is not rider skill. The problem is the premise.</div>
<p>The future of horsemanship will not come from better equipment. It will come from better skill, deeper understanding, and communication that works with the horse's mind rather than around it. True partnership requires consent, not domination.</p>
<p>Anything less deserves to be questioned. And if this idea unsettles you — it may be worth asking why.</p>
  """,
  prev=("when-dressage-changed.html", "When Dressage Changed"),
  nxt=("aids-and-cues.html", "Aids and Cues")
)

write_page("aids-and-cues.html",
  "Aids and Cues",
  "The Future",
  "Aids and Cues",
  "The difference changes everything.",
  """
<p>In dressage we talk constantly about aids: inside leg, outside rein, direct and indirect rein, weight shift, even stirrup stepping. The language is technical and precise. There are hundreds of books on the aids, with entire chapters dissecting hand position, leg timing, rein angles and seat bones.</p>
<p>But horses are not born knowing our aids. They are not taught "inside leg to outside rein" by their mothers. They do not read training manuals. They do not arrive understanding collection, lateral work or rein contact. Everything must be learned from scratch.</p>
<p>And yet there are almost no books on how to read what the horse is telling you back.</p>
<h2>The Distinction</h2>
<p>An aid is something the rider does. A cue is something the horse understands. The aid is the physical action: the closing of the leg, the movement of the hand, the shift of the seat. It exists whether the horse understands it or not. A cue, however, exists inside the horse's nervous system. It is not something you apply. It is something the horse has learned to associate with meaning. A cue only exists once learning has happened.</p>
<p>When you get on a horse, the two of you do not share a language. You share space, weight, pressure and energy — but you do not share meaning. There is no built-in translation system. You have to establish a dialogue from the ground up.</p>
<h2>The Mouth and the Contact</h2>
<p>A horse's mouth is extraordinarily sensitive. It is richly innervated and designed for delicate tactile discrimination. It does not scar over or "harden" in the way people casually suggest. It remains sensitive. Simply placing a bit in the mouth already creates sensation. Even before the rider moves their hands, there is contact. There is weight. There is presence. That alone is background noise.</p>
<p>If the rider then holds the horse, braces, or fails to follow the natural oscillation of the mouth with an elastic hand, that noise increases. The rein is no longer a clear question; it becomes a continuous stimulus.</p>
<blockquote>Imagine a leaf blower outside your window at six in the morning. It is not a precise instruction. It is an ongoing intrusion.</blockquote>
<p>When contact is constant rather than meaningful, the horse cannot distinguish signal from interference. The aid never becomes a cue because it never stands alone. It is buried in noise. And static cannot become a cue.</p>
<h2>What Refinement Feels Like</h2>
<p>When riding becomes refined, something subtle shifts. The rider is no longer thinking primarily about applying aids. The rider is listening. The physical inputs become quieter because the learned associations are stronger. It begins to feel less like applying pressure to create a response and more like offering information and receiving feedback.</p>
<div class="pull-quote">There may be hundreds of books on how to use the aids. Perhaps the next generation of horsemanship needs more on how to read the horse's cues.</div>
<p>Because until what we do becomes meaningful to them, it is not communication. It is just noise.</p>
  """,
  prev=("her-mouth.html", "Her Mouth, Not Ours"),
  nxt=("no-hard-mouth.html", "There Is No Such Thing as a Hard Mouth")
)

write_page("no-hard-mouth.html",
  "There Is No Such Thing as a Hard Mouth",
  "The Future",
  "There Is No Such Thing as a Hard Mouth",
  "There are only horses who have learned that the hand does not make sense.",
  """
<p>People say it constantly. "He's too strong." "He doesn't listen." "He's heavy in the contact." "He leans on my hands." Then comes the prescription: more straightness, more inside leg, more outside rein, more strength in the hand.</p>
<p>But modern neurobiology tells a very different story.</p>
<h2>What the Mouth Actually Is</h2>
<p>The mouth is not like external skin. It is mucosal tissue. Along with the eyes, nostrils, genitals, and anus, it forms a densely innervated sensory interface connected directly to the autonomic nervous system. These are intimate biological structures evolved for voluntary functions — eating, breathing, social communication, reproduction. They are not designed as control points.</p>
<p>The horse's diastema exists to separate cropping teeth from grinding teeth. The gingiva (gums) do not develop protective calluses. They are highly vascular and designed to heal quickly so that nutrition is never compromised. This tissue is built for sensitivity and rapid recovery — not for the gradual "toughening" riders imagine when they speak of a hard mouth.</p>
<h2>What Does Happen</h2>
<p>What does happen is neural adaptation. If pressure is constant, the nervous system dulls its response in order to cope. If release is late or inconsistent, the horse stops searching for it. If it is unyielding or unrelenting — as constant "contact" is — the horse will shut down to it.</p>
<p>If the leg drives while the hand restrains, the signals contradict one another. If the rider balances on the reins, the horse learns to brace. The horse resolves the conflict the only way available: by adapting. Over time, animals do what animals always do when they cannot escape pressure. Some lean. Some curl behind the contact. Some open their mouths or shake their heads. Some shut down. None of this is hardness. It is accommodation.</p>
<h2>Leverage Does Not Create Understanding</h2>
<p>When riders say a horse has a "hard mouth," what they usually mean is that the rein no longer produces the response they expect. The instinct is to increase leverage. But leverage does not create understanding. It only increases pressure. You can overpower tissue. You cannot overpower a nervous system into genuine softness.</p>
<div class="pull-quote">There is no such thing as a hard mouth. There are only horses who have learned that the hand does not make sense.</div>
<p>If the answer appears to be a stronger bit, the problem is almost never the mouth. It is timing. It is balance. It is clarity. It is training. Blaming the horse for adapting does not solve the problem. It only deepens the misunderstanding.</p>
  """,
  prev=("aids-and-cues.html", "Aids and Cues"),
  nxt=("rewriting-the-rules.html", "Rewriting the Rules")
)

write_page("rewriting-the-rules.html",
  "Rewriting the Rules — or Not?",
  "The Future",
  "Rewriting the Rules — or Not?",
  "The problem has already been solved.",
  """
<p>There is a common assumption that bitless dressage cannot be permitted because the rules do not currently allow it, and that rewriting the rules to incorporate bitless bridles would be too complex or difficult. It is often suggested that judges would struggle to define or evaluate "contact" without the presence of a bit.</p>
<p>In reality, this problem has already been solved.</p>
<h2>The Dutch Solution</h2>
<p>The Dutch equestrian federation — the Koninklijke Nederlandse Hippische Sportfederatie (KNHS) — allows dressage tests to be ridden in approved bitless bridles up to ZZ-Zwaar level (approximately equivalent to Small Tour preparation). Their regulations simply clarify how bitless riding is to be interpreted within the existing judging framework.</p>
<p>Article 147 of the Dutch national dressage rules states:</p>
<blockquote>"Dressage tests may be ridden bitless up to the ZZ-Zwaar level for both horses and ponies. From the Light Tour level onward, participation bitless is permitted only hors concours (HC). In dressage tests ridden bitless, 'contact' as described in the training scale means light contact on the reins with the horse and the horse's head and neck position."</blockquote>
<h2>What This Demonstrates</h2>
<p>In other words, the judging criteria do not change. Judges continue to assess the horse according to the training scale — rhythm, suppleness, connection, impulsion, straightness and collection. The Dutch federation did not need to redesign the sport, rewrite the judging system, or redefine the fundamentals of dressage. They simply clarified that contact refers to the rein connection between horse and rider, rather than specifically to the presence of a bit.</p>
<div class="pull-quote">Dressage judging remains exactly the same: it evaluates the training, balance and way of going of the horse, not the hardware used to ride it.</div>
<p>This demonstrates that incorporating bitless riding into dressage rules is neither complex nor disruptive. The path has been marked. The question is whether other federations — including Dressage Australia — are willing to follow it.</p>
  """,
  prev=("no-hard-mouth.html", "There Is No Such Thing as a Hard Mouth"),
  nxt=("the-day-i-took-the-bit-out.html", "The Day I Took the Bit Out")
)

write_page("the-day-i-took-the-bit-out.html",
  "The Day I Took the Bit Out",
  "The Future",
  "The Day I Took the Bit Out — and Nothing Changed",
  "A cappuccino, a trail ride, and a realisation.",
  """
<p>My journey into bitless riding didn't begin with a philosophy or a training method. It began with a cappuccino.</p>
<p>I was out on a trail ride with Leo and we stopped for coffee. While we were sitting there, I took the bit out of his mouth so he could graze. He was wearing a Rambo Micklem bridle, so I simply unbuckled the bit and left the rest of the bridle on. When it was time to go home, I had a simple thought: I'll just ride him like this and see what happens. If it didn't work, I could always put the bit back in.</p>
<p>But the bit never went back in.</p>
<h2>The Experiment</h2>
<p>Leo never seemed to get the memo that there was no bit in his mouth. He walked off exactly as he always did. He trotted, he cantered, and he even had a gallop. He stopped, he steered, and he listened — to me. Nothing was different. But everything was.</p>
<p>The next day — being a competitive rider — I went into the arena to see what I could and couldn't do. At first my aids were bigger than usual. But something interesting happened. His leg yields were better. Shoulder-in was better. His little half-pass was better. Everything that had previously felt like a balance between forward movement and containment was suddenly easy. The handbrake was off.</p>
<p>Once, while riding past the zoo, a group of zebras suddenly trotted towards the fence. Leo got the fright of his life and headed for the hills. In reality he cantered about twenty metres. Then I stopped him. Exactly as I normally would. There was no difference. And from that moment on, the bit simply never went back in his mouth.</p>
<h2>Freya</h2>
<p>Freya is a warmblood — a feisty one who bucks when she is having fun. When I tried to back her one day, she gave me a flying lesson that broke my scapula and five vertebral processes. When I rode her bitless, nothing changed for her either. Control was the same. They walked. They trotted. They stopped. They steered. They jumped. They never got the memo that anything was different.</p>
<h2>The Illusion of Control</h2>
<p>If removing the bit changed almost nothing about my ability to ride the horse, then where was the control actually coming from? My experience suggested that much of what we call control was already coming from somewhere else — from the horse himself. What I had previously attributed to the bit was, in reality, the result of communication and trust. The horse had never been responding primarily to the metal in his mouth. He had been responding to the conversation.</p>
<div class="pull-quote">What I thought was control was actually communication.</div>
<h2>The Intelligence of the Horse</h2>
<p>Horses are extraordinarily intelligent animals. They learn patterns quickly. They read body language with astonishing accuracy. They are highly sensitive to balance, tension, intention, and rhythm. They are not machines waiting to be sculpted. They are partners capable of understanding.</p>
<p>Removing the bit did not magically transform my horses. What it did was reveal something that had been there all along. The control I believed the bit was providing had largely been an illusion. The real control — if we want to call it that — had always come from somewhere else. Not from the bit. But from something far simpler: understanding, communication, and the intelligence of the horse.</p>
  """,
  prev=("rewriting-the-rules.html", "Rewriting the Rules"),
  nxt=None
)

# ── BLOG INDEX ─────────────────────────────────────────────────────────────────
blog_posts = [
    ("the-1850-model.html", "18 Feb 2026", "The 1850 Model of Biological Hierarchy Is Still With Us", "The nineteenth century formalised a worldview that shaped institutions, industry, and horsemanship alike."),
    ("his-mouth-blog.html", "13 Feb 2026", "His Mouth, Not Ours", "The mouth belongs to the horse. It is not sporting equipment, not a training interface, not a steering wheel."),
]

blog_cards = ""
for fname, date, title, excerpt in blog_posts:
    blog_cards += f"""
<a href="{fname}" style="display:block;background:var(--forest-mid);padding:2.5rem;text-decoration:none;transition:background .3s;margin-bottom:2px;" onmouseover="this.style.background='var(--forest-light)'" onmouseout="this.style.background='var(--forest-mid)'">
  <span class="blog-date">{date}</span>
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.6rem;font-weight:300;color:var(--cream);margin-bottom:.8rem;line-height:1.2;">{title}</h3>
  <p style="color:var(--gold-pale);opacity:.75;font-size:.95rem;line-height:1.7;margin:0;">{excerpt}</p>
  <span style="display:inline-block;margin-top:1.2rem;font-family:'Cinzel',serif;font-size:.55rem;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;">Read More &rarr;</span>
</a>"""

blog_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Blog | Dressage for the Future</title>
{FONTS}{SHARED_CSS}
</head>
<body>
{NAV}
<div class="article-hero">
  <span class="section-label">Writing</span>
  <h1 class="article-title">From the Blog</h1>
  <p class="article-subtitle">Essays, observations, and arguments from the field.</p>
</div>
<div class="gold-rule"></div>
<div style="background:var(--forest);padding:4rem 8%;">
{blog_cards}
</div>
{FOOTER}
</body></html>"""
with open(f"{OUT}/blog.html", "w") as f:
    f.write(blog_html)
print("✓ blog.html")

# ── BLOG POSTS ─────────────────────────────────────────────────────────────────
write_page("the-1850-model.html",
  "The 1850 Model of Biological Hierarchy Is Still With Us",
  "Blog — 18 Feb 2026",
  "The 1850 Model of Biological Hierarchy Is Still With Us",
  "Written by Paula Lasersohn",
  """
<p>Biological hierarchies are rarely limited to one domain. The nineteenth century formalised a worldview that shaped institutions, industry, and horsemanship alike. It was a model of biological and racial hierarchy. Men were placed above women. Humans were placed above animals. Authority was strength. Empathy was weak. Control was treated as morally superior to attachment. Obedience was a moral virtue.</p>
<p>Dominance was considered natural. Distance was considered necessary. Emotion was considered a liability.</p>
<p>This framework made sense within its historical context. Cavalry systems required obedience. Industrial culture valued efficiency. Animals were widely understood as mechanical bodies rather than sentient nervous systems. But although the language has softened, the structure of that worldview has not entirely disappeared. It resurfaces whenever affection is framed as the problem.</p>
<h2>The Gendered Undertone</h2>
<p>From time to time we hear the claim that the fundamental issue in modern riding is sentimental ownership — that women mix love with a lack of education. The phrasing may shift, but the underlying assumption remains: love undermines authority, emotion dilutes standards, and discipline must be reclaimed from softness. This is not simply a training opinion. It is an ideological inheritance.</p>
<p>Education and attachment are not opposites. Modern learning theory, across species, is built on clarity of signals, reinforcement history, timing, and regulation of the nervous system. A chronically threatened animal does not learn more efficiently. Sustained stress impairs cognitive flexibility and increases conflict behaviours. None of this supports the idea that emotional distance improves training outcomes.</p>
<p>The majority of modern horse owners are women. Many are highly educated. They invest in veterinary consultation, biomechanics, saddle science, nutrition, and welfare metrics. To suggest that the central problem of riding is female affection echoes an older hierarchy in which rational authority is coded masculine and emotional attachment is coded feminine — and inferior.</p>
<h2>What Education Actually Requires</h2>
<p>Even the dismissal of food reinforcement as "corruption" reflects this moral framing. Reinforcement science is not sentimentality. It is a defined behavioural mechanism grounded in decades of research. The question is not which tool is morally superior. The question is why compassion is so often treated as evidence of incompetence.</p>
<p>If the industry struggles, the causes are structural: competitive incentives, economic pressures, tradition, spectacle, and the slow integration of welfare science. These are not the consequence of women loving their horses.</p>
<div class="pull-quote">Love is not the threat to horsemanship. Unexamined hierarchy is.</div>
<p>Education evolves. It absorbs neuroscience, stress physiology, pain research, and advances in behavioural science. When education refuses to update itself, it stops being education. It becomes preservation. Dressage for the Future is not an argument for indulgence or the removal of standards. It is an argument for updating them.</p>
<p>The 1850 model may still echo in our language. It does not have to shape our future.</p>
<p class="blog-author" style="margin-top:3rem;">— Paula Lasersohn</p>
  """,
  prev=None,
  nxt=("his-mouth-blog.html", "His Mouth, Not Ours")
)

write_page("his-mouth-blog.html",
  "His Mouth, Not Ours",
  "Blog — 13 Feb 2026",
  "His Mouth, Not Ours",
  "Written by Paula Lasersohn",
  """
<p>The mouth belongs to the horse. It is not sporting equipment, not a training interface, not a steering wheel, not a balancing aid or a psychological support system for the rider. It is living tissue. It is sensory. It is neurological. It is how horses explore the world, regulate themselves, connect socially, graze, soothe, and communicate.</p>
<p>Through the mouth they select forage, taste minerals, separate sand from feed, drink, groom, and calm themselves. It is not an accessory attached to the horse. It is part of the nervous system itself.</p>
<p>Placing a bit inside it is therefore not neutral. Applying pressure through it is not neutral. Strapping it shut is not neutral. Controlling an animal's body through one of its most sensitive sensory regions can never be neutral. Tradition does not make it neutral. Habit does not make it neutral.</p>
<h2>Necessity and Pleasure</h2>
<p>We accept invasive acts when they are necessary. Animals are restrained for medical treatment. Surgery is performed to save life. These are grave compromises justified by survival or welfare. But sport is not necessity. Competition is not necessity. Our hobbies, ambitions, lessons, and beach rides are not necessity. Pleasure does not justify invasion of another body.</p>
<p>For centuries horses were treated as mechanical beings — bodies governed by weight and force rather than minds and agency. Within that worldview domination felt rational. Control could be mistaken for refinement. Compliance could be mistaken for understanding. But that worldview no longer survives serious scientific scrutiny.</p>
<h2>A Different Conversation</h2>
<p>Modern biology and cognitive science recognise horses as intelligent, perceptive, emotionally responsive mammals. They learn through prediction, pattern, and relationship. They possess memory, fear, preference, curiosity, and social awareness. They are not force systems awaiting correction. Once that is understood, the conversation changes.</p>
<div class="pull-quote">This is not a debate about softer hands or gentler contact. It is about ownership. The horse's body belongs to the horse.</div>
<p>The future of horsemanship will not come from better equipment. It will come from better skill, deeper understanding, and communication that works with the horse's mind rather than around it. True partnership requires consent, not domination. Anything less deserves to be questioned. And if this idea unsettles you — it may be worth asking why.</p>
<p class="blog-author" style="margin-top:3rem;">— Paula Lasersohn</p>
  """,
  prev=("the-1850-model.html", "The 1850 Model"),
  nxt=None
)

# ── HOW WE GOT HERE landing ────────────────────────────────────────────────────
how_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>How We Got Here | Dressage for the Future</title>
{FONTS}{SHARED_CSS}
</head>
<body>
{NAV}
<div class="article-hero">
  <span class="section-label">History &amp; Context</span>
  <h1 class="article-title">How We Got Here</h1>
  <p class="article-subtitle">Understanding the past is how we build a better future.</p>
</div>
<div class="gold-rule"></div>
<div style="padding:5rem 8%;max-width:900px;margin:0 auto;">
  <p style="color:var(--ink-soft);margin-bottom:3rem;font-size:1.1rem;">Dressage did not arrive at its current form by accident. It was shaped by military necessity, philosophical assumptions about animal consciousness, and the slow commercialisation of equestrian sport. Understanding these forces is the first step toward changing them.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;">
    <a href="before-sentience.html" style="display:block;border-top:2px solid var(--gold);padding-top:1.5rem;text-decoration:none;">
      <span style="font-family:'Cinzel',serif;font-size:.55rem;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;display:block;margin-bottom:.8rem;">Essay</span>
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:var(--forest);margin-bottom:.6rem;">If He Only Had a Brain</h3>
      <p style="font-size:.95rem;color:var(--mist);">The Cartesian roots of force-based training and why they no longer hold.</p>
    </a>
    <a href="when-dressage-changed.html" style="display:block;border-top:2px solid var(--gold);padding-top:1.5rem;text-decoration:none;">
      <span style="font-family:'Cinzel',serif;font-size:.55rem;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;display:block;margin-bottom:.8rem;">Essay</span>
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:var(--forest);margin-bottom:.6rem;">When Dressage Changed</h3>
      <p style="font-size:.95rem;color:var(--mist);">From art to sport to industry — tracing the transformation of classical dressage.</p>
    </a>
  </div>
</div>
{FOOTER}
</body></html>"""
with open(f"{OUT}/how-we-got-here.html", "w") as f:
    f.write(how_html)
print("✓ how-we-got-here.html")

# ── THE FUTURE landing ─────────────────────────────────────────────────────────
future_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Future | Dressage for the Future</title>
{FONTS}{SHARED_CSS}
</head>
<body>
{NAV}
<div class="article-hero">
  <span class="section-label">Ethics &amp; Evolution</span>
  <h1 class="article-title">The Future</h1>
  <p class="article-subtitle">What ethical dressage looks like — and how to get there.</p>
</div>
<div class="gold-rule"></div>
<div style="padding:5rem 8%;max-width:900px;margin:0 auto;">
  <p style="color:var(--ink-soft);margin-bottom:3rem;font-size:1.1rem;">The future of dressage is not a rejection of the past. It is a recalibration — absorbing what modern science tells us about horse cognition, welfare, and consent, and building methods that reflect that knowledge.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;">
    <a href="her-mouth.html" style="display:block;border-top:2px solid var(--gold);padding-top:1.5rem;text-decoration:none;">
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:var(--forest);margin-bottom:.6rem;">Her Mouth, Not Ours</h3>
      <p style="font-size:.95rem;color:var(--mist);">On the mouth as neurological organ — not equipment.</p>
    </a>
    <a href="aids-and-cues.html" style="display:block;border-top:2px solid var(--gold);padding-top:1.5rem;text-decoration:none;">
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:var(--forest);margin-bottom:.6rem;">Aids and Cues</h3>
      <p style="font-size:.95rem;color:var(--mist);">The difference between what the rider does and what the horse understands.</p>
    </a>
    <a href="no-hard-mouth.html" style="display:block;border-top:2px solid var(--gold);padding-top:1.5rem;text-decoration:none;">
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:var(--forest);margin-bottom:.6rem;">There Is No Such Thing as a Hard Mouth</h3>
      <p style="font-size:.95rem;color:var(--mist);">What riders call hardness is accommodation. The distinction matters.</p>
    </a>
    <a href="rewriting-the-rules.html" style="display:block;border-top:2px solid var(--gold);padding-top:1.5rem;text-decoration:none;">
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:var(--forest);margin-bottom:.6rem;">Rewriting the Rules — or Not?</h3>
      <p style="font-size:.95rem;color:var(--mist);">The Dutch federation has already solved the bitless problem. Others can too.</p>
    </a>
    <a href="the-day-i-took-the-bit-out.html" style="display:block;border-top:2px solid var(--gold);padding-top:1.5rem;text-decoration:none;">
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:var(--forest);margin-bottom:.6rem;">The Day I Took the Bit Out</h3>
      <p style="font-size:.95rem;color:var(--mist);">A personal account of riding bitless — and what it revealed about control.</p>
    </a>
  </div>
</div>
{FOOTER}
</body></html>"""
with open(f"{OUT}/the-future.html", "w") as f:
    f.write(future_html)
print("✓ the-future.html")

# ── ABOUT ──────────────────────────────────────────────────────────────────────
about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About | Dressage for the Future</title>
{FONTS}{SHARED_CSS}
</head>
<body>
{NAV}
<div class="article-hero">
  <span class="section-label">About</span>
  <h1 class="article-title">My Work</h1>
  <p class="article-subtitle">I work for the horses.</p>
</div>
<div class="gold-rule"></div>
<div class="article-body">
  <p>At the intersection of equine welfare, communication, and performance, my focus is simple: a horse's body belongs to the horse. The work is finding ways to implement and influence those around us. Everything I do — writing, riding, training and competing — is grounded in that principle.</p>
  <h2>Advocacy &amp; Content Creation</h2>
  <p>I create written and visual work exploring the horse's mouth as a neurological organ — not equipment. Like the eyes, nostrils, genitals, and anus, the mouth is mucosal, highly innervated tissue directly connected to the autonomic nervous system. Control devices inserted into such tissue — particularly for entertainment or sport — deserve ethical scrutiny.</p>
  <p>My work examines how tradition, language, and habit have shaped what we consider "normal" in equestrian sport — and invites riders to think differently. I am also actively involved in challenging local and federal government on the concept of sentience and bodily integrity.</p>
  <h2>Competitive Riding</h2>
  <p>I compete in showjumping and remain undecided about dressage and eventing because I do not like riding with a bit. As the rules currently stand, competing in those disciplines requires one. I am therefore working to find a balance that feels ethical for both me and my horses.</p>
  <p>I am also actively engaged with Dressage Australia to advocate for the inclusion of bitless bridles. Performance and welfare are not opposites. When communication is clear, work becomes easier — not harder — and jump-offs faster.</p>
  <p>My aim is not to criticise from the sidelines, but to show — practically and publicly — that another way is possible.</p>
  <h2>About Paula</h2>
  <p>I'm Paula Lasersohn — rider, horsewoman, and lifelong student of how horses think, feel, and learn. I am neurodivergent and deeply empathetic, which shapes how I experience horses. I do not see them as animals to be managed. I experience them as intelligent beings with nervous systems, emotions, and opinions.</p>
  <p>Dressage for the Future grew out of my own struggle to reconcile classical ideals with modern competitive scoring — and a fundamental question I couldn't ignore: how could a "positive contact" possibly be pleasant for the horse?</p>
  <p>I am becoming an Equestrian Australia accredited coach and have competed internationally in eventing, and in dressage to Prix St Georges. I have showjumped, raced thoroughbreds, played polocross, and won multiple South African Championships across disciplines. My background gives me a deep understanding of classical training systems — and it's precisely that experience that led me to question them.</p>
  <p>I'm also an accredited WOW saddle fitter and barefoot trimmer, which gives me a whole-horse perspective on comfort, movement, and long-term soundness.</p>
  <p>Over a lifetime in horses, I've had hundreds — likely thousands — of lessons with exceptional horsemen, including Morten Thomsen, Jean-Philippe Cambourlives, Maud Aarts, Fred de Wae, Daniel Pevsner, Hans Staub and Andreas Hausberger from the Spanish Riding School in Vienna. I've also been fortunate to meet extraordinary horses such as Olympic Bonfire, Olympic Salerno and Olympic Scandic.</p>
  <div class="pull-quote">Some of the most important truths I've learned didn't come from riders at all — but from the horses themselves.</div>
</div>
{FOOTER}
</body></html>"""
with open(f"{OUT}/about.html", "w") as f:
    f.write(about_html)
print("✓ about.html")

# ── CONTACT ────────────────────────────────────────────────────────────────────
contact_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact | Dressage for the Future</title>
{FONTS}{SHARED_CSS}
</head>
<body>
{NAV}
<div class="article-hero">
  <span class="section-label">Get in Touch</span>
  <h1 class="article-title">Contact</h1>
  <p class="article-subtitle">Questions, collaboration, or conversation — all welcome.</p>
</div>
<div class="gold-rule"></div>
<div class="article-body" style="padding-bottom:8rem;">
  <p>If you'd like to get in touch — whether about the ideas here, collaboration, coaching, or advocacy — please reach out directly.</p>
  <p>Paula Lasersohn<br>Canberra, Australia<br>
  <a href="mailto:contact@dressageforthefuture.com">contact@dressageforthefuture.com</a></p>
  <p>You can also follow the work at <a href="https://www.dressageforthefuture.com">dressageforthefuture.com</a>.</p>
</div>
{FOOTER}
</body></html>"""
with open(f"{OUT}/contact.html", "w") as f:
    f.write(contact_html)
print("✓ contact.html")

print("\nAll pages built successfully!")

# ══════════════════════════════════════════════════════════════════════════════
# ADDITIONAL PAGES FROM SCRAPED CONTENT
# ══════════════════════════════════════════════════════════════════════════════

write_page("consent.html",
  "Consent",
  "The Future",
  "Consent",
  "When consent is impossible, ethics become stricter — not weaker.",
  """
<p>Horses cannot give consent in the human sense. They cannot understand long-term ambitions such as competition, prestige, or sport. They cannot weigh risk against reward, negotiate terms, or meaningfully withdraw permission once a system is in motion.</p>
<p>Some people take this fact and draw a convenient conclusion: if horses cannot consent, then consent is irrelevant. If left to choose, they would rather eat grass than work. Therefore everything we do with them is forced, and the ethical question disappears.</p>
<p>This is a logical failure.</p>
<div class="pull-quote">When consent is impossible, ethics do not weaken. They become stricter.</div>
<p>This principle is widely recognised in ethics: when one party cannot consent, the duty of care on the other becomes greater, not smaller. In every serious ethical domain — medicine, education, animal welfare — the inability to consent increases the responsibility of the one who holds power. The question shifts from "Did they agree?" to "Is this justified?"</p>
<h2>What Consent Looks Like in Practice</h2>
<p>If a being cannot consent, we ask different questions. Not "Did they agree?" but: Is this necessary? Is this the least invasive option available? Is the being's experience being taken seriously? Would a reasonable, informed advocate for this being approve?</p>
<p>These are not soft questions. They are the framework used in medical ethics for patients who cannot speak for themselves, in legal systems for those who cannot represent themselves, and in animal welfare science for beings whose experience matters but whose voice cannot be heard in human terms.</p>
<p>Applied to horses, these questions become practical and specific. Is the training method chosen because it is genuinely the most effective and least harmful — or because it is traditional, convenient, or fast? Is the horse's experience monitored beyond the absence of catastrophic injury? Is discomfort being managed, minimised, and justified?</p>
<h2>Consent Signals</h2>
<p>Horses communicate constantly. They show curiosity, willingness, tension, fear, confusion, relaxation, and resistance. These are not random. They are information. A horse that is tense in the back, high in the neck, short in the stride, and tight in the jaw is telling us something. A horse that swings through, breathes freely, seeks connection, and offers more than was asked is telling us something different.</p>
<p>We may not be able to ask for consent. But we can learn to read the answer.</p>
<p>The future of ethical horsemanship is not about abandoning the work. It is about taking the horse's experience seriously enough to let it guide how the work is done. That is not sentimentality. It is the minimum that the science of welfare now demands.</p>
  """,
  prev=("aids-and-cues.html", "Aids and Cues"),
  nxt=("meaningful-measurable.html", "Meaningful and Measurable")
)

write_page("meaningful-measurable.html",
  "Meaningful and Measurable",
  "The Future",
  "Meaningful and Measurable",
  "Meaningful to whom? To those who cannot consent.",
  """
<p>Riders, spectators, sponsors, and judges all have opinions about what constitutes good dressage. The horse does not get a vote. And yet the horse is the one whose body, nervous system, and daily experience are most directly affected by what "good dressage" means in practice.</p>
<p>Welfare claims in equestrian sport are often impressionistic. A horse "looks happy." A horse "loves its job." The contact is "soft." The training is "classical." These claims are not meaningless — but they are not evidence. They are assertions. And assertions made by people with a financial, competitive, or reputational interest in a particular outcome are not a reliable guide to the horse's actual experience.</p>
<h2>What Measurement Requires</h2>
<p>Meaningful welfare assessment requires measurable indicators that are independent of the observer's interest. These exist. They include cortisol levels, heart rate variability, behavioural stress indicators, postural tension markers, facial action coding, and ethological assessments of conflict behaviour.</p>
<p>None of these are routinely required in competition. None are part of the standard judging framework. The FEI Dressage Rules reference welfare extensively — but the enforcement mechanisms rely almost entirely on visible, catastrophic injury. Subclinical stress, chronic tension, and cumulative psychological cost are not measured and are rarely penalised.</p>
<h2>The Standard We Should Apply</h2>
<p>The question "Is this horse okay?" should not be answered by the rider, the trainer, or the judge. It should be answered by the evidence. What does the horse's body show? What do behavioural indicators reveal? What would an independent welfare assessor, using current scientific tools, conclude?</p>
<p>Dressage claims to place welfare at its centre. The gap between that claim and the current measurement framework is wide. Closing it is not an attack on the sport. It is the minimum that taking the claim seriously requires.</p>
  """,
  prev=("consent.html", "Consent"),
  nxt=("the-age-of-intelligence.html", "The Age of Intelligence")
)

write_page("the-age-of-intelligence.html",
  "The Age of Intelligence",
  "The Future",
  "The Age of Intelligence",
  "Not our intelligence — theirs.",
  """
<p>The Age of Intelligence demands a change in the status quo. We now know better and must do better. We can no longer rely on Cartesian thinking and dogma. The military order and discipline must change — not from discipline to chaos, not from structure to indulgence, but from coercion to cognition.</p>
<p>Pressure may introduce a behaviour, but understanding sustains it. We know that the horse is a sentient, thinking, intelligent animal and must now start treating them like one.</p>
<h2>When the Horse Participates Mentally</h2>
<p>When the horse participates mentally, responses become lighter. Regulation improves. Welfare is measurable, not assumed. This is not softness — it is efficiency. A horse that understands does not need to be managed. A horse that thinks does not need escalating pressure.</p>
<h2>Fading the Aid</h2>
<p>All aids should be temporary. They are for learning, not performance. Once a horse knows how to do something there is no need to keep asking in the same way. The aid should fade — from strong to light, from obvious to invisible, from external to internal. The goal is always self-carriage: the horse maintaining the movement, the balance, and the frame without constant input from the rider.</p>
<p>This is not a new idea. The classical masters described it. Descente de main — the giving of the hand — was the test of true collection. The horse that fell apart when the rein was softened had not truly learned. The horse that maintained its balance and carriage had.</p>
<h2>The Intelligent Horse</h2>
<p>Modern neuroscience confirms what the best horsemen always suspected: horses are capable of far more than simple conditioned response. They form expectations. They solve problems. They recognise patterns across contexts. They remember — accurately and over long periods. They have preferences. They have aversions. They have relationships with specific people that influence how they learn.</p>
<p>A training system that treats the horse as a reflex machine is not just ethically questionable. It is technically inefficient. It produces horses that comply under pressure and fall apart when pressure is removed. It produces horses that are managed rather than trained.</p>
<p>The age of intelligence is not a sentiment. It is a methodology. It asks us to build training systems worthy of the animal we are working with.</p>
  """,
  prev=("meaningful-measurable.html", "Meaningful and Measurable"),
  nxt=("control-vs-cooperation.html", "Control vs Cooperation")
)

write_page("control-vs-cooperation.html",
  "Control vs Cooperation",
  "The Future",
  "Control vs Cooperation",
  "Dressage is often described as control. But control is a strange word for a relationship between two nervous systems.",
  """
<p>A horse is not a vehicle. It is not a machine. It is a learning animal. And learning animals do not perform because they are controlled. They perform because they understand.</p>
<h2>The Traditional Model</h2>
<p>Traditional riding systems often rely on opposing forces. Leg driving forward. Hand containing the power. The horse is pushed into the contact and held there. This produces spectacular movement. But it also creates a permanent tension between two signals: Forward. Stop. The horse resolves that contradiction the only way animals can — by adapting. By bracing. By finding a way to live inside the contradiction.</p>
<p>The resulting movement can be impressive. But it is not free. It is contained. And contained movement is not the same as movement that arises from genuine understanding and willingness.</p>
<h2>The Cooperation Model</h2>
<p>Modern learning science tells a different story. Animals learn through timing, release, predictability, and clarity. When signals are consistent and understandable, behaviour becomes voluntary. The horse begins to offer the correct response not because it is forced to, but because it has learned that this is what the signal means — and because the outcome is predictable and the pressure is released.</p>
<p>In a cooperation model, the rider's job is not to contain power. It is to direct understanding. The aids are not forces to be applied — they are signals to be learned. Collection is not the result of hand and leg opposing one another. It is the result of the horse genuinely shifting its balance — because it understands that this is what is being asked, and because it has the physical ability to do it.</p>
<h2>What This Looks Like in Practice</h2>
<p>A horse trained through cooperation does not fall apart when the rein is released. It maintains its balance because the balance is real — not the artificial product of two opposing forces momentarily in equilibrium. A horse trained through cooperation can be ridden with lighter aids over time, not heavier ones. The aids fade because the understanding deepens.</p>
<p>This is not a utopian vision. It is the goal that the classical tradition always described — and that modern learning science now gives us the tools to achieve more reliably than intuition alone ever could.</p>
  """,
  prev=("the-age-of-intelligence.html", "The Age of Intelligence"),
  nxt=("the-welfare-of-the-horse.html", "The Welfare of the Horse")
)

write_page("the-welfare-of-the-horse.html",
  "The Welfare of the Horse",
  "The Future",
  "The Welfare of the Horse",
  '"If they said what they meant and meant what they said — then they\'d be faithful 100%"',
  """
<h2>Revised FEI Code of Conduct for the Welfare of the Horse</h2>
<p>The Fédération Équestre Internationale affirms that the welfare of the horse is paramount. Paramount means that the physical and mental wellbeing of the horse shall take precedence over competitive success, commercial interest, reputational considerations, or institutional convenience.</p>
<p>Welfare shall be defined in accordance with contemporary animal welfare science, including the Five Freedoms framework and the Five Domains Model. Welfare is not defined solely by the absence of catastrophic injury. Welfare includes the horse's physical health, behavioural freedom, and cumulative mental state over time.</p>
<h2>Article 1 — Foundational Welfare Standards</h2>
<h3>1.1 Freedom from Pain, Injury and Disease</h3>
<p>Horses must not be entered into training or competition when there is evidence of clinical or subclinical pathology, inflammatory stress indicating elevated injury risk, or behavioural signs of acute or chronic pain including but not limited to: resistance, tension, conflict behaviours, abnormal oral behaviours, or avoidance of work.</p>
<h3>1.2 Freedom from Fear and Distress</h3>
<p>Training and competition environments must not subject horses to stimuli that cause acute fear responses, sustained psychological distress, or learned helplessness. Evidence of such conditions — including stereotypies, hyper-vigilance, shutdown behaviour, or consistent conflict behaviour under saddle — must be treated as welfare indicators requiring investigation, not as training problems to be overcome through escalating pressure.</p>
<h3>1.3 Freedom to Express Normal Behaviour</h3>
<p>Horses must have access to turnout, social contact, forage, and movement sufficient to support normal behavioural expression. Housing conditions that prevent these must not be considered acceptable on grounds of competition convenience or facility limitation.</p>
<h2>Article 2 — Training Standards</h2>
<h3>2.1 Progressive Training</h3>
<p>Training must follow a progressive, evidence-based framework. Escalating pressure without a corresponding increase in the horse's understanding and voluntary compliance is not progressive training — it is coercion. Coercion that produces apparent compliance through suppression rather than understanding is not dressage. It is management of a stressed animal.</p>
<h3>2.2 Prohibited Training Techniques</h3>
<p>The following techniques are prohibited at all times: hyperflexion (rollkur) beyond brief use for specific therapeutic purposes verified by a veterinarian; training to a consistent position behind the vertical; use of equipment designed to restrict the horse's ability to raise or extend the head and neck during work; use of draw reins, side reins, or similar equipment in a manner that creates a fixed frame rather than supporting self-carriage.</p>
<h2>Article 3 — Competition Standards</h2>
<h3>3.1 Judging Criteria</h3>
<p>Judging must reward self-carriage, lightness, and genuine relaxation. Movement produced through containment of opposing forces — leg against hand — rather than through genuine balance and impulsion must not receive high marks. A horse showing signs of tension, resistance, or conflict behaviour cannot be considered to demonstrate correct dressage regardless of the extravagance of its movement.</p>
<h3>3.2 Welfare Monitoring</h3>
<p>All major competitions must include independent welfare assessment by qualified professionals not affiliated with the competing combinations. Welfare assessors must have authority to request veterinary examination and to recommend withdrawal of a combination where welfare concerns exist.</p>
<div class="pull-quote">The welfare of the horse is not a marketing statement. It is a commitment. It requires enforcement mechanisms, measurable standards, and the willingness to act when the evidence demands it.</div>
<p>The gap between what the FEI currently states and what it currently enforces is wide. This document represents what the stated commitment would actually require if taken seriously.</p>
  """,
  prev=("control-vs-cooperation.html", "Control vs Cooperation"),
  nxt=None
)

# ── BLOG POSTS ─────────────────────────────────────────────────────────────────

write_page("the-patience-pole.html",
  'The "Patience Pole"',
  "Blog",
  'The "Patience Pole"',
  "Horses cannot consent in any meaningful way. Does that make what we do to them acceptable?",
  """
<p>Horses cannot consent in any meaningful way. They cannot understand what we want from them in the long term, cannot negotiate, and cannot meaningfully refuse once a system of training is in motion. This is sometimes used to argue that the question of consent is irrelevant.</p>
<p>The patience pole is a device used to tie a horse in a fixed position — often in a bent or uncomfortable posture — for extended periods. The stated purpose is to teach the horse to stand still, to accept restraint, or to "think." The actual mechanism is learned helplessness. The horse learns not that restraint is acceptable, but that resistance is futile.</p>
<p>This is not training in any meaningful sense. It is the systematic removal of the horse's ability to respond to discomfort. The horse does not learn that standing still is safe. It learns that it cannot escape. The behaviour that follows — apparent calmness, reduced movement, reduced resistance — looks like acceptance. It is shutdown.</p>
<h2>The Difference Between Acceptance and Shutdown</h2>
<p>An animal that has genuinely accepted a situation shows normal physiological indicators. Its heart rate is stable. Its cortisol is unremarkable. It can be distracted by other stimuli. It responds to release. A horse in learned helplessness shows a different profile. It may appear calm on the surface while showing elevated stress hormones, reduced responsiveness, and conflict behaviour when the situation changes.</p>
<p>We are very good at mistaking the second for the first. Stillness looks like acceptance. Reduced resistance looks like willingness. But the horse's internal experience may be the opposite of what the surface suggests.</p>
<p>The patience pole produces stillness. It does not produce acceptance. And training built on the suppression of the horse's response is not partnership. It is the systematic removal of the horse's ability to communicate.</p>
  """,
  prev=None,
  nxt=("totilas.html", "Totilas")
)

write_page("totilas.html",
  "Totilas",
  "Blog",
  "Oh The Horse That Could Fly",
  "A poem about what we celebrated — and what we missed.",
  """
<blockquote>
Oh hushity-hush in the big shiny hall —<br>
Totilas, Totilas, best horse of all!<br>
He piaffe'd and passage'd and floated on air,<br>
The crowd held its breath at the sight of him there.
</blockquote>
<p>Totilas was perhaps the most celebrated dressage horse of the modern era. His scores were unprecedented. His movement was extraordinary. He was sold for a reported €10 million — the most expensive dressage horse in history at the time.</p>
<p>He was also a horse who, by many accounts, was not enjoying himself.</p>
<p>The tension visible in his top line, the tightness in his jaw, the restricted neck — these are not the signs of a horse in self-carriage. They are the signs of a horse working against containment. The extravagance of his movement was real. The freedom was not.</p>
<p>Totilas represents something important about modern dressage: the gap between what looks spectacular and what is correct. Between what impresses the crowd and what is good for the horse. Between the score on the board and the horse's internal experience.</p>
<p>He was not a villain. His connections were not monsters. They were working within a system that rewards a certain kind of movement regardless of how it is produced. The system is the problem. Totilas was its most visible product.</p>
<div class="pull-quote">What we celebrated in Totilas was brilliance. What we failed to ask was: at what cost?</div>
<p>That question — at what cost? — is the one that dressage now needs to take seriously. Not to punish the past, but to build a better future.</p>
  """,
  prev=("the-patience-pole.html", 'The "Patience Pole"'),
  nxt=("a-faulty-premise.html", "A Faulty Premise")
)

write_page("a-faulty-premise.html",
  "A Faulty Premise",
  "Blog",
  "A Faulty Premise",
  "Classical dressage has surged in popularity. But is the premise it rests on correct?",
  """
<p>Classical dressage has surged in popularity among horse-lovers who are dissatisfied with modern sport dressage. The rollkur scandals, the Helgstrand footage, the increasingly mechanical quality of top-level competition — these have pushed many riders toward the classical tradition as an ethical alternative.</p>
<p>This instinct is understandable. Classical dressage does emphasise lightness, self-carriage, and harmony. Its language is more concerned with the horse's balance and freedom than with spectacle and power. In many ways it is genuinely better.</p>
<p>But classical dressage rests on a premise that deserves examination: that the methods developed before we understood equine cognition, neuroscience, and welfare science are the correct methods — and that modern deviation from them is the problem.</p>
<h2>What the Classical Tradition Got Right</h2>
<p>The classical masters were extraordinarily observant. Working without the tools of modern science, they developed methods through careful attention to the horse's responses over decades of practice. Many of their observations hold up well when examined through a contemporary lens. The emphasis on relaxation, rhythm, and self-carriage reflects genuine understanding of how horses move most efficiently. The insistence on lightness aligns with what we now know about how pressure affects learning.</p>
<h2>What It Got Wrong</h2>
<p>But the classical tradition also contains methods, assumptions, and techniques that do not survive scientific scrutiny. Some of its tools cause pain. Some of its timelines are based on tradition rather than evidence. Some of its language — about submission, about dominance, about the horse "accepting" the rider — reflects the philosophical assumptions of its era rather than what we now know about equine psychology.</p>
<p>The faulty premise is not that classical dressage is bad. It is that classical dressage, simply by virtue of being classical, is correct. Age is not evidence. Tradition is not validation. The question is not whether something is old — it is whether it is true, whether it works, and whether the horse's experience of it is acceptable by the standards we now hold.</p>
<div class="pull-quote">Classical dressage is a better starting point than modern sport dressage. It is not the finishing line.</div>
  """,
  prev=("totilas.html", "Totilas"),
  nxt=("but-is-it-classical.html", "But Is It Classical?")
)

write_page("but-is-it-classical.html",
  "But Is It Classical?",
  "Blog",
  "But Is It Classical?",
  "No, definitely not — and that might not be the right question.",
  """
<p>Traditional classical dressage rests on foundations that are worth examining honestly. The question "but is it classical?" is one of the most common defences offered in equestrian discussions. A technique is questioned. A method is challenged. And the response is: but this is how it has always been done. This is the classical way.</p>
<p>This is an appeal to tradition. And an appeal to tradition is not an argument.</p>
<h2>What Classical Actually Means</h2>
<p>The classical tradition in dressage refers to a body of knowledge developed over several centuries, primarily in European courts and military academies, by riders and trainers working with horses for specific practical purposes. It is a tradition of extraordinary sophistication and remarkable horsemanship.</p>
<p>It is also a tradition that predates our understanding of equine neuroscience, stress physiology, learning theory, and welfare science. It was developed by people who believed, in many cases, that horses were animals of limited intelligence whose cooperation was obtained through discipline and repetition rather than genuine understanding.</p>
<p>Some of what the classical tradition produced is genuinely excellent — and holds up well when examined against modern knowledge. Some of it does not. Treating the tradition as a monolithic authority that cannot be questioned is not classical. It is dogma.</p>
<h2>The Better Question</h2>
<p>The better question is not "is it classical?" The better question is: does it work? Is it ethical? Does it respect what we now know about the horse's experience? Can it be justified by evidence rather than by precedent?</p>
<p>A technique that is classical but causes pain is not thereby acceptable. A technique that is modern but produces genuine lightness, relaxation, and self-carriage is not thereby suspect. The test is the horse. The test is always the horse.</p>
<div class="pull-quote">The classical tradition is a resource. It is not an answer. The answer is always in front of you — in the horse you are riding today.</div>
  """,
  prev=("a-faulty-premise.html", "A Faulty Premise"),
  nxt=None
)

print("\n✓ All additional pages built!")
