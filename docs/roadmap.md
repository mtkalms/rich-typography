# Roadmap

This roadmap is more a collection of ideas and a rough sketch of the direction I want to take rich-typography in rather than a concrete plan.


- [ ] Fonts

    - [x] Sans
    - [x] Serif
    - [x] Semi Serif
    - [ ] Slab Serif
    - [ ] Script
    - [ ] Blackletter/Fraktur
    - [ ] Handwriting
    - [ ] Monospace

- [ ] Typefaces

    Bundle fonts into typefaces to customize the other ANSI styles (bold, italic, etc.).
    This depends on whether it is possible to form these variants with common unicode characters.

- [ ] Font file import/export
    - [x] `.toff` import
    - [ ] `.toff` export
    - [ ] Figlet import/export

        Figlet fonts are not completely compatible with rich-typography.
        However, they could serve as a useful starting point for creating custom fonts.

        For now use [rich-pyfiglet][rich-pyfiglet] and [textual-pyfiglet][textual-pyfiglet] for all your figlet needs.

- [ ] Font editor

    Creating fonts by copy and paste from a unicode table is a pain.
    A bespoke textual application for creating and editing fonts would be great.
    
    For now use [ASCII Motion][ascii-motion] to sketch out your ideas.
    
- [ ] Animations

    - [ ] Line Animations
    - [ ] Typewriter effect
    - [ ] Customize blink ANSI style
    
    
[ascii-motion]: https://ascii-motion.app/
[rich-pyfiglet]: https://github.com/edward-jazzhands/rich-pyfiglet
[textual-pyfiglet]: https://github.com/edward-jazzhands/textual-pyfiglet