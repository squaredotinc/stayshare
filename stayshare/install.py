import frappe

class Datum:
    def __init__(self, name, type, desc=None) -> None:
        self.name = name
        self.type = type
        self.desc = desc

def seed_data():
    amenity = "amenity"
    loc = "location"
    house = "house"
    
    amenities = [
        Datum("ceiling", amenity),
        Datum("security", amenity, "gate, durawall, dogs, neighborhood watch, guards.."),
        Datum("solar", amenity),
        Datum("water backup", amenity, "borehole, tank"),
        Datum("parking", amenity),
        Datum("family", amenity),
        Datum("singles", amenity),
        Datum("gender", amenity),
        Datum("couple", amenity),
        Datum("BIC", amenity),
        Datum("tiles", amenity),
        Datum("ensuite", amenity),
        Datum("time restriction", amenity),
        Datum("pets", amenity)
    ]   
    
    houses = [
        Datum("Flat | Bedsitter | Bachelor Pad", house),
        Datum("Room", house, "individual rooms..single or double rooms"),
        Datum("Cottage", house),
        Datum("Full House", house),
    ]  
    
    locations = [
        Datum("Harare CBD", loc),
        Datum("Hatfield", loc),
        Datum("Mufakose Hre", loc),
        Datum("Eastlea Hre", loc),
        Datum("Avondale Hre", loc),
        Datum("Waterfalls Hre", loc),
        Datum("Bulawayo CBD", loc),
    ]   
    
    items = amenities + houses + locations 
    
    count = 0
    
    for item in items:
        try:
            ss_item = frappe.get_doc({
                "doctype": "SS Item",
                "item_name": item.name,
                "type": item.type,
                "description": item.desc
            })
            
            ss_item.insert(ignore_permissions=True)
            
            count += 1
        
        except Exception as err:
            frappe.log(f"failed to add item: {item} | error: {err}")
            continue
        
    frappe.log(f"StayShare install hook: processed {count} items")
 
@frappe.whitelist()
def after_install():
    try:
        seed_data()
    except:
        frappe.log_error(title='StayShare hook error')