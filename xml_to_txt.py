import glob
import lxml.etree as ET
def xml_to_txt(file):
    alto_namespace = "http://www.loc.gov/standards/alto/ns-v4#"
    nsmap = {"alto": alto_namespace}  # the default namespace (no prefix)
    tree = ET.parse(file)
    lines = tree.xpath("//alto:String/@CONTENT", namespaces=nsmap)
    print(lines)

    with open(file.replace("xml", "txt"), "w") as output_file:
        [output_file.write(f"{line}\n") for line in lines]

if __name__ == '__main__':
    [xml_to_txt(file) for file in glob.glob("*.xml")]