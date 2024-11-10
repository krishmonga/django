module.exports = {
    content: [
      './templates/**/*.html',           // For template files in the templates folder
      './theme/templates/**/*.html',      // If theme app has a templates directory
      './**/*.html',                      // To catch all HTML files in the project
      './djangoapp/templates/**/*.html',  // If djangoapp has template files
      './theme/static/js/**/*.js',        // JavaScript files (if any)
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  };
  