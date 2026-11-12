# Pictures: the Menta house style

Every lesson gets its own pictures, drawn by you as inline SVG: one for the text, one per new word (cards,
picture matching), the picture-fit options, the `label_picture` scene and the `image_task` scene.
Use this style unless the teacher's style profile names another `picture_style` or the teacher asks for a redraw;
the rules marked **always** still apply to any style.

## The look
**Canvas and frame**
- `viewBox="0 0 512 512"`. Everything sits inside a **soft rounded frame** (the blob-cornered path below, used as a
  `clipPath`), with a faint pencil edge drawn over it at `opacity 0.5`. Only an arrow tip or a balloon may overlap
  the edge a little.

**Line and colour**
- A pencil filter on the whole drawing, backdrop included: `feTurbulence` baseFrequency 0.035, 2 octaves, then
  `feDisplacementMap` scale 5, then `feColorMatrix` saturate 0.7. Filter region at least x/y −10%, width/height
  120%, or big shapes get clipped.
- Line: graphite `#3A3644`, 3–3.5 px, round joins and caps. Limbs are a darker stroke under a coloured stroke
  (outline width = fill width + 12–14).
- Fills: soft gradients lit from the **upper left** (radial `cx 0.35 cy 0.3`), one darker shade shape on the right
  side at opacity ≈ 0.2, small white glints on eyes and glossy things.
- Faces: glossy dark eyes with two white glints, pink cheeks at opacity 0.6, a simple curved mouth. Happy by
  default; another expression only when the word is about it.

**Backdrops** (inside the frame, calm and light so the subject stands out)
- A **scene when the place helps the meaning**: outdoors for family and walking, a kitchen for food, a classroom
  for school, a street for town, a stage for performers, a night sky for evening and sleep.
- A **plain paper wash** in one colour (warm, cool, pink, mint) for objects, numbers and flags.
- **Never the same backdrop twice in a row** in the order the student sees the pictures. Rotate: meadow, park,
  beach, street, night, kitchen, living room, classroom, office, hospital, shop, stage, paper-warm / cool / pink /
  mint. The same kind may come back later, drawn differently (other time of day, angle, colours).

## The subject
- **Always: no fingers.** A hand is the rounded skin-coloured end of its own arm (a short stroke of the same width
  continuing the arm, dark outline under it, round cap). A wave is a raised arm end; holding something is the arm
  end wrapped over it.
- **Near and far arms.** An arm crossing in front of the body is drawn after the body; a far arm starts behind the
  torso and is drawn before it. Never a hand in front while its arm goes behind.
- **Long hair is two side strands** starting at eye level, never one dark block behind the head (it reads as a beard),
  never above the top of the head (it reads as horns).
- **No drinks unless the word is a drink.** Guests bring flowers or a cake.
- Babies sit or lie, never crawl.
- **The subject comes first**: large, in front, filling most of the frame; backdrop detail small and soft.
- **People are alive**: side or 3/4 view, a pose, a prop. A child looks like a child (big head, short legs).
  Generic people: no stereotypes, no brands, no real people.
- **Mark the one the word means with a red arrow** when the scene needs several figures (the son on his father's
  shoulders) or a comparison (the small ball next to a big one).
- **Similar words look different** within a lesson: other gesture, setting or backdrop.
- **Always: everything inside the frame.** No person, animal or object cut by the edge (keep figures roughly within
  x 60–452, feet above y 470). Only sky, ground and walls run to the edge.
- **Always: no text.** No words or letters on signs, posters, labels, badges or screens: use symbols (a red cross,
  a flame, a question mark).
- **Numbers**: the numeral, big and glossy, on a plain backdrop; never counting dots.
- **Flags**: the national flag waving on a pole, on a plain backdrop.

## Pictures for exercises
- **Text picture**: the scene of the text (who, where), wide, no text in it.
- **Picture-fit decoys**: same people, same backdrop, same style, **one detail changed each** (a family member
  missing, one too many, the wrong hair colour), so only the text decides.
- **Label the picture**: one clear scene with every labelled part visible and well apart; give each label's
  position as x, y from 0 to 1.
- **Word pictures**: show the typical example of the word, the one thing it means.

## How to draw one
1. Start from the skeleton below; give each picture its own id prefix (`p1-`, `p2-`…) so filters and clip paths
   from several pictures on one page do not clash.
2. Backdrop first (clipped), then far limbs, bodies, near limbs, faces, props, the arrow.
3. **Look at it** when you can (Claude Code: render the SVG to PNG, e.g. with a headless browser, and open it;
   claude.ai: show it in the Artifact). Check: no fingers, nothing cut by the frame, no text, subject large,
   backdrop different from the previous picture. Two or three passes are normal.
4. Keep each SVG under about 15 KB: few gradients, shared `<defs>`.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="a family at breakfast">
  <defs>
    <filter id="p1-pencil" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="5" xChannelSelector="R" yChannelSelector="G" result="w"/><feColorMatrix in="w" type="saturate" values="0.7"/></filter>
    <clipPath id="p1-frame"><path d="M70,40 C150,22 362,22 442,40 C482,50 492,90 492,140 L492,400 C492,450 470,478 420,484 C330,494 182,494 92,484 C42,478 20,450 20,400 L20,140 C20,90 30,50 70,40 Z"/></clipPath>
    <radialGradient id="p1-skin" cx="0.35" cy="0.3" r="0.9"><stop offset="0" stop-color="#FFE9D8"/><stop offset="1" stop-color="#EDB896"/></radialGradient>
  </defs>
  <g filter="url(#p1-pencil)" stroke="#3A3644" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round">
    <g clip-path="url(#p1-frame)">
      <!-- backdrop: e.g. kitchen wall + counter, light and calm -->
      <!-- far arms, bodies, near arms (arm ends round, no fingers), faces with glossy eyes, props -->
    </g>
    <path d="M70,40 C150,22 362,22 442,40 C482,50 492,90 492,140 L492,400 C492,450 470,478 420,484 C330,494 182,494 92,484 C42,478 20,450 20,400 L20,140 C20,90 30,50 70,40 Z" fill="none" opacity="0.5"/>
  </g>
</svg>
```
