import 'server-only'
 
const locales = {
  en: () => import('./locale/en.json').then((module) => module.default),
}
 
export const getLocale = async (locale) => locales[locale]()