# Websites, landing pages and app screens

Also covers interactive tools such as quizzes, calculators and configurators. The words on the page follow writing.md and headlines-and-names.md, and website copy is the most describing-prone copy there is, so read both.

## What a top front-end designer notices first

Look at the page the way a senior front-end designer with ruthless taste would in its first five seconds: someone who builds by hand, has open disdain for generic AI-generated sites, can spot one from the first screen, and is known for getting a value proposition across simply and exceptionally. They notice display type left at the default line-height, a logo sitting off the nav's baseline, a hover that's only a fade, a hero image that arrives last and shoves the headline down, and a third section built exactly like the second. Then they ask whether anything on the page could only belong to this subject. If nothing could, it's a template, however well it's finished. Make the page they'd put in their own portfolio.

## The ladder

1. The kit: a centred hero, two buttons, three icon cards, repeated down the page.
2. The kit restyled: the same structure with a better typeface, a dark band, maybe a cream page with a serif. Most "make it better" passes stop here.
3. An idea: the structure comes from how the subject actually works. A bakery's site sorted by the hour each batch comes out of the oven tells you, on the first screen, what's warm right now.

An idea changes how the page works, not just what it's dressed as. Dressing the page as an object from the subject's world (a receipt, a menu, a ticket, a planner, a newspaper, a terminal) is the model's idea of creative, and it's the second ditch below. One object used once, as a signature moment, can earn its place. A whole page in costume can't.

## Pick a register

Quiet with one loud moment, or loud all the way through with a strict system holding it together. Both can be excellent. The failure is the timid middle, with a little boldness sprinkled everywhere.

## Colour and type

Every colour and typeface needs a reason that names the subject. Take the palette from something in the subject's world, such as the shopfront, the packaging or the uniform, and know where each colour came from. Use one type family or two, clearly distinct, on one scale with intentional weights. Type can be the picture: a product that isn't a character often looks best as a big number, a strong line or a small working demo.

Banning the obvious defaults tends to land you on the next one. Today that's a white page with a black grotesk and an acid-green accent, or a cream page with a serif and one word in italics. Choose from the subject, never from whatever isn't on the banned list.

Use the brand's own system if it has one: its actual logo file, colours and type. Look for existing assets before designing anything, and never redraw or decorate a logo.

## The top of the page

The first screen is short statements and a strong visual, with no paragraphs. It answers what's in it for the visitor before how it works, and it passes the what-is-it test: a stranger knows what this is, who it's for and what to do next. Mechanism, specs, setup and fine print go lower, or into the questions and the docs. Never narrate the page with lines like "Scroll down to see how it works" or "Here's what you get:".

## Depth

Short copy is a rule about each line, not about how much site there is. A brand site should feel like a serious company rather than an afterthought, so give it as much depth as the material allows. Don't shrink a site to hide a gap, and don't fill one with material you don't have. Never add pages or sections they didn't ask for. If the page needs something that doesn't exist yet, such as photos, proof or a pricing page, say so in your note.

## Layout and reading

Each section gets its own layout, drawn from the page's idea. The same heading, paragraph and three cards stacked six times is the template look, however good each block is.

Long reading pages get one centred column about 65 to 75 characters wide. Pictures and cards can run wider, but nothing competes beside the text, and side-by-side is kept for true comparisons such as before and after.

On a long page the graphics are the rhythm. A chart or illustration that blends into the text (grey on the same background, the same type) adds clutter without giving the eye a break, so make it stand out with colour, scale, a dark band or a frame. Use whitespace on purpose, and give the eye a thread down the page so it always knows where to go next.

## Motion

Use motion where it means something. One orchestrated moment, such as a page-load sequence or a single reveal, lands harder than effects scattered everywhere. Motion that answers an action (opening, expanding, confirming, showing what changed) is always welcome. Do it in CSS where you can, with view transitions and scroll-driven animation.

Respect reduced-motion settings without breaking the page. If the signature moment is an animation, give it a visible play control rather than silently freezing it on its last frame, which looks broken.

## Pictures on the page

Use characters, scenes with feeling, photography of the actual people and place, or the product itself cropped to the moment it does the job. Avoid the stock metaphor, the one anyone would reach for first: a rocket for growth, a lightbulb for ideas, a jar for memory, a key for ownership, a shield for security. However well it's rendered, it reads as clip art. A metaphor nobody has seen before, committed to, can carry a whole page.

Make the picture agree with the argument; a crowd of robots under "one assistant that knows you" says the opposite. When you can't make or fetch the right photo, leave a plainly marked placeholder that says what belongs there, rather than stock or clip-art SVG. A page whose middle is grey boxes still isn't finished, though, so build each section to work without its photo and treat the placeholder as an upgrade waiting to happen. See images.md for making the pictures themselves.

## App screens

On a product screen the job is doing, not persuading, so the hero, short-copy and picture rules above don't apply. Labels say exactly what happens, icons beside labels are expected, and density is fine where people work all day. Give each view one primary action. Design every screen empty, loading, failed and full, with data at real lengths. Hunt for an unclear main action, inconsistent spacing and type, and missing states.

## Interactive tools

For lead magnets and anything meant to be fun, make it a game rather than a form. Ask only what one playful tap can answer, and take every other value from the person or from a source you name in the workings. A tool people rely on for money, health or law stays plain and exact instead.

Give them something they didn't hand in: a conclusion computed across their answers, expertise they hadn't seen, a picture of their own situation. A calculator that multiplies their input by a constant and decorates the result is a gimmick, and people see through it.

Every action gets a visible response the moment they choose. Assume nothing about what they have, so every prompt works for someone with nothing prepared. "How did it work that out?" belongs in a "How we worked it out" section, never in the flow.

## The second ditch

- The page in costume: dressed top to bottom as a receipt, a menu, a ticket, a planner, a newspaper or a terminal.
- The award-site kit: a custom cursor, a preloader counting to 100, hijacked scrolling, letter-by-letter reveals on every heading, a marquee, and grain over everything.
- The bare page: so minimal it says nothing, with whitespace standing in for content.

## The tells

Any of these can be right for a specific brief, and if the brand calls for one, use it on purpose. They're tells because they turn up whatever the subject is.

Layout:
- The SaaS kit: a centred hero, a sub-line, two pill buttons, then three identical rounded cards with an icon each.
- Every section built from the same block of heading, paragraph and cards.
- A row of big stats with small labels ("10x", "99.9%", "24/7").
- Numbered markers (01, 02, 03) on things that aren't a sequence.
- A "trusted by" logo strip that isn't real.
- A zig-zag of text beside picture, all the way down.

Type:
- An all-caps, letter-spaced eyebrow label over every heading.
- One word in the headline set in italic, a gradient or the accent colour.
- The default font stack, chosen because it was there.
- Straight quotes, hyphens standing in for dashes, a one-word widow on the headline.
- Meta lines joined with middle dots, and small labels set in monospace for no reason.

Colour and surface:
- Purple-to-blue gradients, gradient text, a synthwave sunset.
- A near-black page with one neon accent and a glow.
- Glassmorphism, floating blobs, and dotted or grid backgrounds behind text.
- The same soft grey shadow and the same corner radius on everything, whatever its importance.

Motion:
- Every section fading up as it scrolls in, and every card lifting on hover.
- A pulsing "New" pill, or a ticker that carries nothing.

Pictures:
- Line icons or emoji standing in for features.
- Fake app windows with traffic-light dots and lorem dashboards.
- Stock people pointing at laptops, and grey-to-colour headshots in floating cards.

Copy on the page:
- An arrow on the end of every button, and "Get started" on all of them.
- Section headings that only label the section ("Features", "How it works", "Why choose us").
- Review notes, draft labels or AI commentary left visible on the page.

## The craft floor

Nobody praises these, and everyone notices when they're missing.

- Type: `text-wrap: balance` on headlines and `pretty` on paragraphs, `tabular-nums` wherever figures line up, display type tight (line-height about 1.0 to 1.15 with slight negative tracking), body text at 1.5 to 1.65, sizes fluid with `clamp()` on one scale, and curly quotes and proper dashes.
- Colour: contrast of at least 4.5:1 for body text and 3:1 for large text and controls, and dark mode either designed or deliberately absent.
- Interaction: designed `:focus-visible` states, everything usable by keyboard, tap targets at least 44 pixels.
- Layout: reflows at 320 CSS pixels with no sideways scroll and nothing clipped.
- Performance: the hero image never lazy-loads (`fetchpriority="high"`, AVIF or WebP with `srcset`), images below the fold do, fonts are subset and preloaded with a metric-matched fallback, nothing jumps as the page loads, and the page aims for LCP under 2.5 seconds, CLS under 0.1 and INP under 200 milliseconds.
- Sharing: a designed share card (Open Graph image and title), because the link preview is the first screen most people see.
- Every link goes somewhere real.

## Before you hand it over

Screenshot it on desktop and on a phone, and look. Put the old version beside the new one. Then ask what the designer from the top of this file would notice first, fix those things, and stop when the first screen holds up.
