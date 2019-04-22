def generateSetXML(set_id, mms_id, holding_id, item_id, barcode):
    set_xml = \
f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<set link="https://api-na.hosted.exlibrisgroup.com/almaws/v1/conf/sets/{set_id}">
  <id>{set_id}</id>
  <number_of_members link="https://api-na.hosted.exlibrisgroup.com/almaws/v1/conf/sets/{set_id}/members">1</number_of_members>
<members total_record_count="1">
  <member link="https://api-na.hosted.exlibrisgroup.com/almaws/v1/bibs/{mms_id}/holdings/{holding_id}/items/{item_id}">
    <id>{item_id}</id>
    <description>{barcode}</description>
  </member>
</members>
</set>"""

    return set_xml