// Entry and rule titles have ids like `good-problem-framing-rule-2-h`, but the id the book tells readers to cite is on
// the wrapping article or section (`good-problem-framing-rule-2`). Point Starlight's heading anchor links there.
// Starlight adds its anchor links in a rehype plugin it registers during config setup, so this one is registered by an
// integration listed after starlight() to run later. The headings keep their ids, so "On this page" still works.
const idOf = (node) => {
	if (node.type === 'element') return node.properties && node.properties.id;
	if (node.type === 'mdxJsxFlowElement' || node.type === 'mdxJsxTextElement') {
		const a = (node.attributes || []).find((x) => x.name === 'id' && typeof x.value === 'string');
		return a && a.value;
	}
};

const isAnchorLink = (node) => {
	if (node.type !== 'element' || node.tagName !== 'a') return false;
	const p = node.properties || {};
	return [].concat(p.className || [], String(p.class || '').split(/\s+/)).includes('sl-anchor-link');
};

export function rehypeCanonicalAnchors() {
	return (tree) => {
		const walk = (node, ids) => {
			const id = idOf(node);
			const inner = id ? new Set(ids).add(id) : ids;
			if (isAnchorLink(node)) {
				const m = String(node.properties.href || '').match(/^#(.+)-h$/);
				if (m && ids.has(m[1])) node.properties.href = '#' + m[1];
			}
			(node.children || []).forEach((c) => walk(c, inner));
		};
		walk(tree, new Set());
	};
}

export default function canonicalAnchors() {
	return {
		name: 'dfg-canonical-anchors',
		hooks: {
			'astro:config:setup': ({ config }) => {
				const plugins = config.markdown.processor && config.markdown.processor.options.rehypePlugins;
				if (!Array.isArray(plugins)) throw new Error('dfg-canonical-anchors needs the unified Markdown processor');
				plugins.push(rehypeCanonicalAnchors);
			},
		},
	};
}
