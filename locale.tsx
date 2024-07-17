"use server"
 
const locales = {
  en: () => import('./locale/en.json').then((module) => module.default),
  jp: () => import('./locale/jp.json').then((module) => module.default)
}
 
export const getLocale = async (locale) => locales[locale]()