/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['"Playfair Display"', 'serif'],
      },
      colors: {
        navy: '#0F172A',
        slate: '#475569',
        'brand-blue': '#70B2D4',
        'brand-yellow': '#FDBA18'
      }
    },
  },
  plugins: [],
}
