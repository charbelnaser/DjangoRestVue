// frontend/src/plugins/vuetify.js
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import { md3 } from 'vuetify/blueprints'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

export default createVuetify({
  blueprint: md3,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
  theme: {
    defaultTheme: 'myCustomTheme',
    themes: {
      myCustomTheme: {
        dark: false,
        colors: {
          background: '#f5f7fa',
          surface: '#ffffff',
          primary: '#1e88e5',   // Blue
          secondary: '#ff4081', // Pink
          error: '#f44336',
          info: '#2196f3',
          success: '#4caf50',
          warning: '#fb8c00',
        },
      },
    },
  },
})
