import sveltePreprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: sveltePreprocess(),

	kit: {
        // hydrate the <div id="svelte"> element in src/app.html
        target: '#svelte',
        adapter: adapter({
            pages: '../build',
			assets: '../build',
			fallback: null
        }),

        vite: {
            css: {
                preprocessorOptions: {
                    scss: {
                        additionalData: "@import \"src/variables.scss\";"
                    }
                }
            }
        }
    }
};

export default config;
