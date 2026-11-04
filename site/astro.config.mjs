// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkHeadingId from './src/plugins/remark-heading-id.mjs';
import canonicalAnchors from './src/plugins/rehype-canonical-anchors.mjs';
import sidebar from './src/sidebar.json' with { type: 'json' };

const fonts = 'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:wght@300;400;500&family=JetBrains+Mono:wght@400;500;600&display=swap';

export default defineConfig({
	markdown: { remarkPlugins: [remarkHeadingId] },
	devToolbar: { enabled: false },
	integrations: [
		starlight({
			title: 'Design Field Guide',
			description: 'How to design interfaces, and why the good ones work, with a live demo for every idea.',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/ryan-di/design-field-guide' }],
			head: [
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' } },
				{ tag: 'link', attrs: { rel: 'stylesheet', href: fonts } },
			],
			customCss: ['./src/styles/book.css', './src/styles/theme.css', './src/styles/anchors.css'],
			components: {
				Hero: './src/components/Hero.astro',
				PageTitle: './src/components/PageTitle.astro',
				ThemeSelect: './src/components/ThemeToggle.astro',
				Search: './src/components/Search.astro',
			},
			tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
			sidebar,
		}),
		canonicalAnchors(),
	],
});
