from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.AboutBoxBranding'
setup(name='enigma2-plugin-systemplugins-aboutboxbranding',
       version='3.0',
       description='Display box branding info',
       package_dir={pkg: 'AboutBoxBranding'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
