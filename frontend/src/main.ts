import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import 'bootstrap-icons/font/bootstrap-icons.min.css'
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import { plugin, defaultConfig } from '@formkit/vue'
import { generateClasses } from '@formkit/themes'
import { formkitConfig } from './utils/formkitConfig'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.use(
  plugin,
  defaultConfig({
    config: {
      classes: generateClasses(formkitConfig)
    }
  })
)

app.mount('#app')
