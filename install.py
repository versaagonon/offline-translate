import argostranslate.package
import argostranslate.translate

available_packages = argostranslate.package.get_available_packages()
#change "id" and "en" to your language codes
package_to_install = next(
    filter(
        lambda p: p.from_code == "id" and p.to_code == "en",
        available_packages
    )
)
download_path = package_to_install.download()
argostranslate.package.install_from_path(download_path)

print("Model Indonesian -> English already install!")
