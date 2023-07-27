import xml.etree.ElementTree as ET

# Crear la estructura básica del archivo XML
root = ET.Element("KeePassFile")
ET.SubElement(root, "Configuration")
ET.SubElement(root, "Root")
tree = ET.ElementTree(root)

# Guardar el archivo XML inicial
tree.write("database.xml", encoding="utf-8", xml_declaration=True)

# Leer el archivo XML y obtener el elemento raíz
tree = ET.parse("database.xml")
root = tree.getroot()

# Agregar una nueva cuenta a la base de datos
group_element = root.find(".//Group[@Name='Homebanking']")

if group_element is not None:
    entry_element = ET.SubElement(group_element, "Entry")

    ET.SubElement(entry_element, "UUID").text = "new-uuid"
    ET.SubElement(entry_element, "String", attrib={"Key": "Title"}).text = "New Entry"
    ET.SubElement(entry_element, "String", attrib={"Key": "UserName"}).text = "new_username"
    ET.SubElement(entry_element, "String", attrib={"Key": "Password", "ProtectInMemory": "True"}).text = "new_password"
    ET.SubElement(entry_element, "String", attrib={"Key": "URL"}).text = "https://example.com"
    ET.SubElement(entry_element, "String", attrib={"Key": "Notes"}).text = "Additional Notes"
    ET.SubElement(entry_element, "AutoType", attrib={"Enabled": "True"})
    ET.SubElement(entry_element, "History")

# Guardar los cambios en el archivo XML
tree.write("database.xml", encoding="utf-8", xml_declaration=True)

# Leer y mostrar todas las cuentas de la base de datos
for entry_element in root.findall(".//Entry"):
    title = entry_element.find(".//String[@Key='Title']").text
    username = entry_element.find(".//String[@Key='UserName']").text
    password = entry_element.find(".//String[@Key='Password']").text
    url = entry_element.find(".//String[@Key='URL']").text
    notes = entry_element.find(".//String[@Key='Notes']").text

    print("Title:", title)
    print("Username:", username)
    print("Password:", password)
    print("URL:", url)
    print("Notes:", notes)
    print("-------------------")


# import xml.etree.ElementTree as ET
# import io
# import zipfile

# # Crear la estructura básica del archivo XML en un buffer en RAM
# root = ET.Element("KeePassFile")
# ET.SubElement(root, "Configuration")
# ET.SubElement(root, "Root")
# xml_buffer = io.BytesIO()  # Creamos un buffer en RAM
# tree = ET.ElementTree(root)
# tree.write(xml_buffer, encoding="utf-8", xml_declaration=True)

# # Leer el buffer para obtener el contenido del archivo XML
# xml_content = xml_buffer.getvalue()

# # Aquí puedes manipular la base de datos XML en la memoria RAM como lo desees

# # Comprimir la base de datos XML en un archivo ZIP
# with zipfile.ZipFile("database.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
#     # Agregar el contenido del archivo XML al archivo ZIP
#     zipf.writestr("database.xml", xml_content)

# # Opcionalmente, si necesitas extraer y trabajar con la base de datos XML del archivo ZIP
# with zipfile.ZipFile("database.zip", "r", zipfile.ZIP_DEFLATED) as zipf:
#     with zipf.open("database.xml") as xml_file:
#         # Leer el archivo XML y obtener el elemento raíz
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         # Aquí puedes manipular la base de datos XML extraída del archivo ZIP como lo desees
