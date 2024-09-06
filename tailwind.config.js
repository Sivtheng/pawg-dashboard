/** @type {import('tailwindcss').Config} */
export const content = [
  './myapp/templates/**/*.html',
  './myapp/static/**/*.js',
  // Add paths to other files where Tailwind classes might be used
];
export const theme = {
  extend: {
    colors: {
      'light-pink': '#F8EDED',
      'orange': '#FF8225',
      'dark-red': '#B43F3F',
      'dark-blue': '#173B45',
    },
  },
};
export const plugins = [];
