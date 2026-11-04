// `## Title {#some-id}` keeps the book's anchor as the heading id instead of a slug of the text.
export default function remarkHeadingId() {
	const visit = (node) => {
		if (node.type === 'heading') {
			const last = node.children[node.children.length - 1];
			const m = last && last.type === 'text' && last.value.match(/\s*\{#([\w-]+)\}\s*$/);
			if (m) {
				last.value = last.value.slice(0, m.index);
				node.data = { ...node.data, hProperties: { ...(node.data && node.data.hProperties), id: m[1] } };
			}
		}
		(node.children || []).forEach(visit);
	};
	return visit;
}
