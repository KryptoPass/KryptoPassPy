import xml.etree.ElementTree as ET
import zipfile
import io
import os

from utility.constants import KryptoPass as KP

Config = None

class _Config():
    def __init__(self, config):
        self.config = config

    def create_config(self):
        xml_buffer = io.BytesIO()

        root = ET.Element("KryptoPass")
        config = ET.SubElement(root, "Configuration")
        meta = ET.SubElement(config, "Meta")
        ET.SubElement(meta, "Version").text = KP.VERSION.value
        ET.SubElement(meta, "Language").text = KP.LANGUAGE.value
        ET.SubElement(meta, "DatabaseName").text = KP.DATABASE_NAME.value
        ET.SubElement(meta, "DatabaseVersion").text = KP.DATABASE_VERSION.value
        ET.SubElement(meta, "Namespace").text = KP.NAMESPACE.value

        generator = ET.SubElement(meta, "Generator")
        ET.SubElement(generator, "Password", {
                      "length": "16",
                      "specials": "True",
                      "upper": "True",
                      "digits": "True",
                      "emojis": "True",
                      "quantum": "False"
                      })

        ET.SubElement(generator, "Passphrase", {
                      "length": "16",
                      "separator": "",
                      "dict": "english",
                      "quantum": "False"
                      })

        ET.SubElement(generator, "Key", {
                      "length": "32",
                      "output": "base64",
                      "quantum": "False"
                      })

        tree = ET.ElementTree(root)

        tree.write(xml_buffer, encoding="utf-8", xml_declaration=True)

        with zipfile.ZipFile(os.path.join(os.getcwd(), "config.kpxc"), "w") as zipf:
            zipf.writestr("configuration.xml", xml_buffer.getvalue(),
                          compress_type=zipfile.ZIP_DEFLATED)
            xml_buffer.close()

def init(config):
    global Config
    Config = _Config(config)
    return Config