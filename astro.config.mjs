import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Заглушка, яка запобігає падінню вбудованого плагіна sitemap у хуку astro:build:done
const safeSitemap = () => ({
  name: '@astrojs/sitemap',
  hooks: {},
});

export default defineConfig({
  site: 'https://namencora.com',
  integrations: [
    safeSitemap(),
    starlight({
      title: 'Namencora Registry',
      description: 'Deterministic architecture registry and canonical namespace ontology.',
      logo: {
        src: './src/assets/logo.svg',
      },
      social: {
        github: 'https://github.com/AltumVector/namencora'
      },
      sidebar: [
        {
          label: 'Overview & Principles',
          items: [
            { label: 'Canonical Manifesto', link: '/' },
            { label: 'Registry Governance', link: '/governance/' }
					,
					{
						label: 'Division 06: Computational Dynamics & Metrology',
						autogenerate: { directory: 'd06' },
					},
          ]
        },
        {
          label: 'Division 00: Core Protocols',
          autogenerate: { directory: 'd00' }
        },
        {
          label: 'Division 01: Storage & Memory',
          autogenerate: { directory: 'd01' }
        },
        {
          label: 'Division 02: Cognitive & Ontological',
          autogenerate: { directory: 'd02' }
        },
        {
          label: 'Division 03: Governance & Consensus',
          autogenerate: { directory: 'd03' }
        },
        {
          label: 'Division 04: Computational Physics',
          autogenerate: { directory: 'd04' }
        },
        {
          label: 'Division 05: Execution Pipelines',
          autogenerate: { directory: 'd05' }
        }
      ]
    })
  ]
});
