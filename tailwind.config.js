/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        customBlue: {
          900: '#020024',
        },
        customNavy: {
          900: '#090979',
        },
        customCyan: {
          400: '#00d4ff',
        },
      },
      backgroundImage: {
      },
    },
  },
  plugins: [],
}
