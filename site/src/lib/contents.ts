import { getCollection } from 'astro:content';
import sidebar from '../sidebar.json';

export interface ContentsPage {
	slug: string;
	title: string;
	number?: string;
	meta: string;
	entries: number;
}

export interface ContentsGroup {
	id: string;
	label: string;
	title: string;
	sub?: string;
	pages: ContentsPage[];
}

const fragments = import.meta.glob<string>('../fragments/**/*.html', { query: '?raw', import: 'default', eager: true });

export async function getContents() {
	const docs = new Map((await getCollection('docs')).map((d) => [d.id, d]));
	const groups: ContentsGroup[] = sidebar.map((group) => {
		const pages = group.items.map(({ slug }) => {
			const doc = docs.get(slug);
			if (!doc) throw new Error(`Sidebar slug ${slug} has no page`);
			const { title, eyebrow = '' } = doc.data;
			const entries = (doc.body ?? '').split('<article class="entry').length - 1;
			const chapter = /^Chapter (\d+)$/.exec(eyebrow)?.[1];
			const meta = entries ? `${entries} ${entries === 1 ? 'entry' : 'entries'}` : eyebrow;
			return { slug, title, number: chapter?.padStart(2, '0'), meta, entries };
		});
		const part = docs.get(group.items[0].slug)?.data.part;
		const [label, rest] = group.label.split(' · ');
		const title = part?.title ?? rest ?? docs.get(group.items[0].slug)?.data.eyebrow ?? group.label;
		for (const page of pages) if (page.meta === title) page.meta = '';
		return { id: part?.id ?? slug(group.label), label, title, sub: part?.sub, pages };
	});
	const pages = groups.flatMap((g) => g.pages);
	const demos = Object.values(fragments).reduce((n, html) => n + (html.match(/class="stage[\s"]/g)?.length ?? 0), 0);
	return {
		groups,
		chapters: pages.filter((p) => p.number).length,
		entries: pages.reduce((n, p) => n + p.entries, 0),
		demos,
	};
}

const slug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-');
