__all__ = [
    'STATE_CHOICES', 'EDUCATIONAL_QUALIFICATION_CHOICES',
    'JobProfilesChoices', 'ExperienceChoices', 'GenderChoice'
]

STATE_CHOICES = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
                 ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
                 ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"),
                 ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"),
                 ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"),
                 ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"),
                 ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"),
                 ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
                 ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
                 ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
                 ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
                 ("Lakshadweep", "Lakshadweep"),
                 ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
                 ("Puducherry", "Puducherry"))

EDUCATIONAL_QUALIFICATION_CHOICES = (
    ('BELOW 5th Class', 'BELOW 5th Class'),
    ('Class 5th to 9th', 'Class 5th to 9th'),
    ('10th pass', '10th pass'),
    ('12th pass', '12th pass'),
    ('ITI', 'ITI'),
    ('Polytechnic', 'Polytechnic'),
    ('Diploma', 'Diploma'),
    ('Graduate (B.Sc., B.A., B.Com.)', 'Graduate (B.Sc., B.A., B.Com.)'),
    ('Other Graduate (Any Stream)', 'Other Graduate (Any Stream)'),
    ('B.Tech. (Any Stream)', 'B.Tech. (Any Stream)'),
    ('M.Tech. (Any Stream)', 'M.Tech. (Any Stream)'),
    ('Post graduate (Any stream)', 'Post graduate (Any stream)'),
    ('MBA/PGDM (Any Stream)', 'MBA/PGDM (Any Stream)')
)


class GenderChoice:
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    choices = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others')
    )


class ExperienceChoices:
    ZERO_TO_6_MONTHS = 0
    SIX_MONTHS_TO_1_YEAR = 1
    ONE_YEAR_TO_2_YEAR = 2
    TWO_YEAR_TO_3_YEAR = 3
    THREE_YEAR_TO_4_YEAR = 4
    FOUR_YEAR_TO_5_YEAR = 5
    ABOVE_5 = 6

    choices = (
        (ZERO_TO_6_MONTHS, '0 to 6 months'),
        (SIX_MONTHS_TO_1_YEAR, '6 months to 1 year'),
        (ONE_YEAR_TO_2_YEAR, '1 year to 2 year'),
        (TWO_YEAR_TO_3_YEAR, '2 year to 3 year'),
        (THREE_YEAR_TO_4_YEAR, '3 year to 4 year'),
        (FOUR_YEAR_TO_5_YEAR, 'Four year to 5 year'),
        (ABOVE_5, 'Above 5')
    )


class JobProfilesChoices:
    MACHINE_OPERATOR_HELPER = '2f0f55'
    IT_ITES = 'b28bda'
    DRIVER_PRIVATE_VEHICLES = 'aa0f20'
    DRIVER_COMMERCIAL_VEHICLES = '4e4c49'
    DRIVER_HEAVY_VEHICLES_BUS_TRUCK_TRAILER_ETC = 'e3b63c'
    BACKHOE_LOADER_OPERATOR = 'fa4771'
    TRACTOR_OPERATOR = 'a141cf'
    SECURITY_STAFF = 'd70763'
    BOUNCER = '8c01b4'
    SECURITY_GUARD_ARMED = 'cdce9e'
    PSO_PERSONAL_SECURITY_OFFICER = '844848'
    COMPUTER_OPERATOR = '00f44e'
    DATA_ENTRY_OPERATOR = 'ab81b3'
    PLUMBER = '42ad1b'
    ELECTRICIAN = 'f09e8a'
    HOUSEKEEPING_STAFF = '538c36'
    RETAIL_SALES_STAFF = 'f468e5'
    RETAIL_STORE_KEEPER = 'dc334b'
    CASHIER = '562ac1'
    SALES_MANAGER = '05bf15'
    FIELD_OFFICER = '17d4c7'
    SUPERVISOR = '14f7c3'
    BEAUTICIAN = 'dc32b9'
    BPO_CALL_CENTRE = '2e309a'
    RECEPTIONIST = '4204b9'
    MANAGEMENT_ADMIN = 'fc9ba4'
    HR = '15e68b'
    ACCOUNTS_EXECUTIVE = '8c92ab'
    GST_EXECUTIVE = '827946'
    ESIC_PF_EXECUTIVE = 'dc6bd4'
    COOK = '0ba34c'
    TAILOR = 'a87dc5'
    DELIVERY_JOBS = '99196d'
    CARPENTER = 'e78e1f'
    PAINTER = '1d6f3b'
    MASON = '4bedce'
    CONSTRUCTION_WORKER = '77f0f6'
    BAR_BINDER = 'f17591'
    WELDER = '751dff'
    CNC_MACHINE_OPERATOR = '2eceeb'
    FITTER = 'c82445'
    DOMESTIC_HELP_MAID_HOMECLEANING = '12a4e7'
    RIDER = 'f53d80'
    AC_REPAIRING_AC_SERVICE = '14dc3d'
    ELECTRONICS_REPAIR = 'e3ad2b'
    HOME_APPLIANCES_REPAIR = '699f02'
    WAITER_RESTAURANT = 'ec2f72'
    BARTENDER = '717f9c'
    HAIR_DRESSER_MALE = '835292'
    HAIR_DRESSER_FEMALE = 'ffa462'
    PERSONAL_ASSISTANT = '8b7a1d'
    PEON = 'f2c3e9'
    DG_OPERATOR = '765812'
    STP_OPERATOR = 'f6a302'
    WTP_OPERATOR = '5a0acd'
    LIFT_OPERATOR = '491d33'
    LIFT_TECHNICIAN = 'e5607f'
    WATER_TANK_CLEANER = 'b32538'
    CAR_WASHER_CLEANER = '0c8e90'
    WEB_DESIGNER = '033ad1'
    WEB_DEVELOPER = '20122b'
    GRAPHIC_DESIGNER = '9cf25f'
    FITNESS_TRAINER = '629513'
    YOGA_TRAINER = '78aaf1'
    LOGISTICS_STAFF_LOADING_UNLOADING = '523e7b'
    PACKAGING_STAFF = '2f7e7a'
    WAREHOUSE_STAFF = '429d1e'
    NURSING_STAFF = '72af59'
    PATIENT_CARE = 'e4ff5b'
    BABY_SITTER_NANNY_MOTHER_CARE = '1c4d2e'
    PARKING_MANAGEMENT_STAFF = '079cdd'
    MST_MULTI_TASKING_STAFF = '21c502'
    HOUSEKEEPING_SUPERVISOR = 'b9ccc8'
    SECURITY_SUPERVISOR = '4fda21'
    TRAINING_SUPERVISOR = '45a587'
    LANDSCAPING_SUPERVISOR = '1ff02d'
    PLUMBING_SUPERVISOR = '5436c9'
    MANPOWER_MOBILISER = '1e6dc7'
    LEATHER_WORKER = 'd265d6'
    DAIRY_WORKER = 'c928e8'
    FACADE_CLEANER = 'f7c1a6'
    BANDBAAJA_STAFF = 'db9e41'
    PARTY_SINGERS = '385cf1'
    OTHER = '1c55d9'

    choices = (
        (MACHINE_OPERATOR_HELPER, 'Machine Operator / Helper'),
        (IT_ITES, 'IT / ITeS'),
        (DRIVER_PRIVATE_VEHICLES, 'Driver (Private Vehicles)'),
        (DRIVER_COMMERCIAL_VEHICLES, 'Driver (Commercial Vehicles)'),
        (DRIVER_HEAVY_VEHICLES_BUS_TRUCK_TRAILER_ETC, 'Driver (Heavy Vehicles - Bus, Truck, Trailer, etc.)'),
        (BACKHOE_LOADER_OPERATOR, 'Backhoe Loader Operator'),
        (TRACTOR_OPERATOR, 'Tractor Operator'),
        (SECURITY_STAFF, 'Security Staff'),
        (BOUNCER, 'Bouncer'),
        (SECURITY_GUARD_ARMED, 'Security Guard (Armed)'),
        (PSO_PERSONAL_SECURITY_OFFICER, 'PSO (Personal Security Officer)'),
        (COMPUTER_OPERATOR, 'Computer Operator'),
        (DATA_ENTRY_OPERATOR, 'Data Entry Operator'),
        (PLUMBER, 'Plumber'),
        (ELECTRICIAN, 'Electrician'),
        (HOUSEKEEPING_STAFF, 'Housekeeping Staff'),
        (RETAIL_SALES_STAFF, 'Retail Sales Staff'),
        (RETAIL_STORE_KEEPER, 'Retail Store Keeper'),
        (CASHIER, 'Cashier'),
        (SALES_MANAGER, 'Sales Manager'),
        (FIELD_OFFICER, 'Field Officer'),
        (SUPERVISOR, 'Supervisor'),
        (BEAUTICIAN, 'Beautician'),
        (BPO_CALL_CENTRE, 'BPO / Call Centre'),
        (RECEPTIONIST, 'Receptionist'),
        (MANAGEMENT_ADMIN, 'Management / Admin'),
        (HR, 'HR'),
        (ACCOUNTS_EXECUTIVE, 'Accounts Executive'),
        (GST_EXECUTIVE, 'GST Executive'),
        (ESIC_PF_EXECUTIVE, 'ESIC / PF Executive'),
        (COOK, 'Cook'),
        (TAILOR, 'Tailor'),
        (DELIVERY_JOBS, 'Delivery Jobs'),
        (CARPENTER, 'Carpenter'),
        (PAINTER, 'Painter'),
        (MASON, 'Mason'),
        (CONSTRUCTION_WORKER, 'Construction Worker'),
        (BAR_BINDER, 'Bar Binder'),
        (WELDER, 'Welder'),
        (CNC_MACHINE_OPERATOR, 'CNC machine operator'),
        (FITTER, 'Fitter'),
        (DOMESTIC_HELP_MAID_HOMECLEANING, 'Domestic Help / Maid /  Home-cleaning'),
        (RIDER, 'Rider'),
        (AC_REPAIRING_AC_SERVICE, 'AC Repairing / AC Service'),
        (ELECTRONICS_REPAIR, 'Electronics Repair'),
        (HOME_APPLIANCES_REPAIR, 'Home Appliances Repair'),
        (WAITER_RESTAURANT, 'Waiter (Restaurant)'),
        (BARTENDER, 'Bartender'),
        (HAIR_DRESSER_MALE, 'Hair Dresser (Male)'),
        (HAIR_DRESSER_FEMALE, 'Hair Dresser (Female)'),
        (PERSONAL_ASSISTANT, 'Personal Assistant'),
        (PEON, 'Peon'),
        (DG_OPERATOR, 'DG Operator'),
        (STP_OPERATOR, 'STP Operator'),
        (WTP_OPERATOR, 'WTP Operator'),
        (LIFT_OPERATOR, 'Lift  Operator'),
        (LIFT_TECHNICIAN, 'Lift Technician'),
        (WATER_TANK_CLEANER, 'Water Tank Cleaner'),
        (CAR_WASHER_CLEANER, 'Car Washer / Cleaner'),
        (WEB_DESIGNER, 'Web Designer'),
        (WEB_DEVELOPER, 'Web Developer'),
        (GRAPHIC_DESIGNER, 'Graphic Designer'),
        (FITNESS_TRAINER, 'Fitness Trainer'),
        (YOGA_TRAINER, 'Yoga Trainer'),
        (LOGISTICS_STAFF_LOADING_UNLOADING, 'Logistics Staff (Loading / Unloading )'),
        (PACKAGING_STAFF, 'Packaging Staff'),
        (WAREHOUSE_STAFF, 'Warehouse Staff'),
        (NURSING_STAFF, 'Nursing Staff'),
        (PATIENT_CARE, 'Patient Care'),
        (BABY_SITTER_NANNY_MOTHER_CARE, 'Baby Sitter / Nanny / Mother Care'),
        (PARKING_MANAGEMENT_STAFF, 'Parking Management Staff'),
        (MST_MULTI_TASKING_STAFF, 'MST (Multi Tasking Staff)'),
        (HOUSEKEEPING_SUPERVISOR, 'Housekeeping Supervisor'),
        (SECURITY_SUPERVISOR, 'Security Supervisor'),
        (TRAINING_SUPERVISOR, 'Training Supervisor'),
        (LANDSCAPING_SUPERVISOR, 'Landscaping supervisor'),
        (PLUMBING_SUPERVISOR, 'Plumbing Supervisor'),
        (MANPOWER_MOBILISER, 'Manpower Mobiliser'),
        (LEATHER_WORKER, 'Leather Worker'),
        (DAIRY_WORKER, 'Dairy Worker'),
        (FACADE_CLEANER, 'Facade Cleaner'),
        (BANDBAAJA_STAFF, 'Band-Baaja Staff'),
        (PARTY_SINGERS, 'Party Singers'),
        (OTHER, 'Other'),
    )
