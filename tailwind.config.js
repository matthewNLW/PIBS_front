/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['Marcellus', 'serif'],
      },
      colors: {
        navy: '#0F172A',
        slate: '#475569',
        'brand-blue': '#188cec',
        'brand-yellow': '#ffde00',
        'brand-yellow-dark': '#ffcf1c',
      }
    },
  },
  plugins: [],
}
