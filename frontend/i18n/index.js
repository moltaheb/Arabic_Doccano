export default {
  locales: [
    {
      name: 'Englishssss',
      code: 'en',
      iso: 'en-CA',
      file: 'en'
    },
    {
      name: '中文',
      code: 'zh',
      iso: 'zh-CN',
      file: 'zh'
    },
    {
      name: 'Français',
      code: 'fr',
      iso: 'fr-CA',
      file: 'fr'
    },
    {
      name: 'Deutsch',
      code: 'de',
      iso: 'de-DE',
      file: 'de'
    }
	{
      name: 'العربية',
      code: 'ar',
      iso: 'ar-SA',
      file: 'ar'
    }
  ],
  lazy: true,
  langDir: 'i18n/',
  defaultLocale: 'en',
  vueI18n: {
    fallbackLocale: 'en'
  },
  detectBrowserLanguage: {
    useCookie: true,
    cookieKey: 'i18n_redirected',
    onlyOnRoot: true // for SEO purposes
  }
}
