"use server"
 
const locales = {
  en: () => import('./locale/en.json').then((module) => module.default),
  jp: () => import('./locale/jp.json').then((module) => module.default)
}
 
export const getLocale = async (locale) => locales[locale]()

export const getLanguageDetails = async (currentLocale) => {
  const localeData = await getLocale(currentLocale)
  const otherLangNames = localeData.Language.OtherLangName.map(otherLang => ({
    code: otherLang.LanguageCode,
    name: otherLang.Name,
    displayName: otherLang.DisplayLangName
  }))
  return [
    {
      name: localeData.Language.Name,
      code: localeData.Language.Code,
      displayName: localeData.Language.Name
    },
    ...otherLangNames
  ]
}