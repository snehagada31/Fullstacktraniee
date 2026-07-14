# Browser Rendering Basics & Critical Rendering Path

## Objective

To understand how browsers render web pages and analyze rendering performance using Chrome DevTools.

---

## Browser Rendering Pipeline

The browser follows these steps:

HTML
↓
DOM

CSS
↓
CSSOM

DOM + CSSOM
↓
Render Tree
↓
Layout
↓
Paint
↓
Composite
↓
Pixels on Screen

---

## Performance Recording

The responsive landing page was recorded using Chrome DevTools Performance panel.

Observed stages:

- Layout
- Paint
- Composite

Screenshots are included in the screenshots folder.

---

## Layout Thrashing (Before)

The first demo repeatedly modified styles and immediately read layout information using `offsetHeight`.

This forced multiple synchronous layout recalculations, increasing rendering work.

Screenshot:
- before-thrashing.png

---

## Optimized Version (After)

The optimized version batched DOM reads and DOM writes separately.

This reduced unnecessary layout calculations and improved rendering performance.

Screenshot:
- after-thrashing.png

---

## Learning Outcomes

- Understood the Browser Rendering Pipeline.
- Learned about the Critical Rendering Path.
- Identified Layout, Paint and Composite events using Chrome DevTools.
- Demonstrated Layout Thrashing.
- Optimized rendering using batched reads and writes.

---

## Conclusion

Efficient DOM manipulation improves browser performance by minimizing unnecessary layout calculations and rendering work.