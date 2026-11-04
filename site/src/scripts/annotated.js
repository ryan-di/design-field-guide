(() => {
  /* Annotated comparisons show both sides at once, so the book's switch leaves them alone. */
  const toggle = window.csToggle;
  window.csToggle = cs => toggle({ querySelectorAll: s => Array.from(cs.querySelectorAll(s)).filter(c => !c.classList.contains('ac')) });

  const anchors = CSS.supports('anchor-name', '--a');
  const shown = el => (el.checkVisibility ? el.checkVisibility({ visibilityProperty: true }) : el.getClientRects().length > 0);
  let uid = 0;

  const side = s => {
    const demo = s.querySelector('.cs-demo'), layer = s.querySelector('.ac-layer');
    const notes = Array.from(s.querySelectorAll('.ac-note'));
    const at = [], rings = [], pins = [], names = [];
    uid++;
    notes.forEach((n, k) => {
      names[k] = '--ac-' + uid + '-' + (k + 1);
      const ring = document.createElement('span'), pin = document.createElement('span');
      ring.className = 'ac-ring'; pin.className = 'ac-pin'; pin.textContent = k + 1;
      ring.style.setProperty('position-anchor', names[k]); pin.style.setProperty('position-anchor', names[k]);
      ring.hidden = pin.hidden = true;
      layer.append(ring, pin); rings.push(ring); pins.push(pin);
    });
    const find = sel => {
      try { const all = Array.from(demo.querySelectorAll(sel)); return all.find(shown) || null; }
      catch (e) { console.warn('annotated: bad selector', sel); return null; }
    };
    const apply = () => {
      notes.forEach((n, k) => {
        const t = find(n.dataset.at), old = at[k];
        if (old && old !== t) { old.style.removeProperty('anchor-name'); old.removeAttribute('data-ac-plain'); }
        if (t) {
          if (anchors && t.style.getPropertyValue('anchor-name') !== names[k]) t.style.setProperty('anchor-name', names[k]);
          if (!anchors && !t.hasAttribute('data-ac-plain')) t.setAttribute('data-ac-plain', '');
        }
        at[k] = t;
        rings[k].hidden = pins[k].hidden = !t || !anchors;
        n.classList.toggle('is-wait', !t);
      });
    };
    let queued = false;
    const later = () => { if (!queued) { queued = true; requestAnimationFrame(() => { queued = false; apply(); }); } };
    new MutationObserver(later).observe(demo, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ['hidden', 'class', 'style', 'open', 'aria-hidden', 'aria-expanded'] });
    ['transitionend', 'animationend', 'toggle'].forEach(e => demo.addEventListener(e, later, true));
    addEventListener('resize', later);

    const hl = k => {
      s.classList.toggle('hl', k >= 0);
      notes.forEach((n, j) => { const on = j === k; n.classList.toggle('on', on); rings[j].classList.toggle('on', on); pins[j].classList.toggle('on', on); });
    };
    const hit = el => at.reduce((best, t, k) => (t && t.contains(el) && (best < 0 || at[best].contains(t)) ? k : best), -1);
    notes.forEach((n, k) => { n.addEventListener('pointerenter', () => hl(k)); n.addEventListener('pointerleave', () => hl(-1)); });
    demo.addEventListener('pointerover', e => hl(hit(e.target)));
    demo.addEventListener('pointerleave', () => hl(-1));
    demo.addEventListener('focusin', e => hl(hit(e.target)));
    demo.addEventListener('focusout', () => hl(-1));
    apply();
  };

  const init = () => document.querySelectorAll('.cs-case.ac .ac-side').forEach(side);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
