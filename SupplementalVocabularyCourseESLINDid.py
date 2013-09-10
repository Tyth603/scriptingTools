__author__ = 'vagrant'
from CourseConfiguration import courseConfiguration


unitNameList = [
"Pertemuan dan Sapaan",
"Bantuan untuk Pembelajaran Bahasa",
"Bantuan Lanjutan untuk Pembelajaran Bahasa",
"Percakapan Sopan",
"Bentuk dan Warna",
"Pakaian",
"Berbelanja dan Toko",
"Rumah dan Apartemen",
"Ruangan di dalam Rumah",
"Keluarga",
"Kantor dan Profesi",
"Bagian Tubuh",
"Kedaruratan",
"Tempat dan Menanyakan Arah",
"Sekolah",
"Instrumen Musik",
"Rekreasi",
"Alam",
"Binatang",
"Makanan 1",
"Makanan 2",
"Pergi ke Restoran",
"Bahasa",
"Negara",
"Perjalanan",
"Membeli Tiket",
"Naik Taksi",
"Menginap di Hotel",
"Pergi ke Bank",
"Angka",
"Hari-hari dalam Seminggu dan Waktu",
"Musim dan Cuaca",
"Kata Ganti Orang dan Kata Sifat Kepunyaan",
"Kata sifat dan Kata keterangan",
"Kata Kerja",
"Preposisi"
]
unitNumbers = {
"Pertemuan dan Sapaan": 1,
"Bantuan untuk Pembelajaran Bahasa": 2,
"Bantuan Lanjutan untuk Pembelajaran Bahasa": 3,
"Percakapan Sopan": 4,
"Bentuk dan Warna": 5,
"Pakaian": 6,
"Berbelanja dan Toko": 7,
"Rumah dan Apartemen": 8,
"Ruangan di dalam Rumah": 9,
"Keluarga": 10,
"Kantor dan Profesi": 11,
"Bagian Tubuh": 12,
"Kedaruratan": 13,
"Tempat dan Menanyakan Arah": 14,
"Sekolah": 15,
"Instrumen Musik": 16,
"Rekreasi": 17,
"Alam": 18,
"Binatang": 19,
"Makanan 1": 20,
"Makanan 2": 21,
"Pergi ke Restoran": 22,
"Bahasa": 23,
"Negara": 24,
"Perjalanan": 25,
"Membeli Tiket": 26,
"Naik Taksi": 27,
"Menginap di Hotel": 28,
"Pergi ke Bank": 29,
"Angka": 30,
"Hari-hari dalam Seminggu dan Waktu": 31,
"Musim dan Cuaca": 32,
"Kata Ganti Orang dan Kata Sifat Kepunyaan": 33,
"Kata sifat dan Kata keterangan": 34,
"Kata Kerja": 35,
"Preposisi": 36,
}

lessonNameToListNameMap = {
"01-Quick-Start": "* 01 - Start Cepat!",
"02-Quick-Start": "* 02 - Start Cepat!",
"03-Quick-Start": "* 03 - Start Cepat!",
"04-Quick-Start": "* 04 - Start Cepat!",
"05-Quick-Start": "* 05 - Start Cepat!",
"06-Quick-Start": "* 06 - Start Cepat!",
"07-Quick-Start": "* 07 - Start Cepat!",
"08-Quick-Start": "* 08 - Start Cepat!",
"09-Quick-Start": "* 09 - Start Cepat!",
"10-Quick-Start": "* 10 - Start Cepat!",
"Adjectives-1": "Kata sifat 1",
"Adjectives-2": "Kata sifat 2",
"Adjectives-3": "Kata sifat 3",
"Adverbs": "Kata keterangan",
"Animals-1": "Binatang 1",
"Animals-2": "Binatang 2",
"Asking-for-Directions-1": "Menanyakan Arah 1",
"Asking-for-Directions-2": "Menanyakan Arah 2",
"Asking-the-Time": "Menanyakan Waktu",
"At-the-Hotel-1": "Di Hotel 1",
"At-the-Hotel-2": "Di Hotel 2",
"At-the-Hotel-3": "Di Hotel 3",
"At-the-Hotel-4": "Di Hotel 4",
"At-the-Restaurant-1": "Di Restoran 1",
"At-the-Restaurant-2": "Di Restoran 2",
"At-the-Restaurant-3": "Di Restoran 3",
"At-the-Restaurant-4": "Di Restoran 4",
"At-the-Restaurant-5": "Di Restoran 5",
"Bathroom-1": "Kamar Mandi 1",
"Bathroom-2": "Kamar Mandi 2",
"Bedroom": "Kamar Tidur",
"Beverages": "Minuman",
"Buying-Tickets-1": "Membeli Tiket 1",
"Buying-Tickets-2": "Membeli Tiket 2",
"Buying-Tickets-3": "Membeli Tiket 3",
"Clothing-1": "Pakaian 1",
"Clothing-2": "Pakaian 2",
"Clothing-3": "Pakaian 3",
"Colors": "Warna",
"Common-Foods": "Makanan Biasa",
"Common-Verbs": "Kata Kerja Biasa",
"Communication-Facilitation-1": "Fasilitasi Komunikasi 1",
"Communication-Facilitation-2": "Fasilitasi Komunikasi 2",
"Communication-Facilitation-3": "Fasilitasi Komunikasi 3",
"Communication-Facilitation-4": "Fasilitasi Komunikasi 4",
"Communication-Facilitation-5": "Fasilitasi Komunikasi 5",
"Communication-Facilitation-6": "Fasilitasi Komunikasi 6",
"Communication-Facilitation-7": "Fasilitasi Komunikasi 7",
"Conjunctions": "Konjungsi",
"Continents": "Benua",
"Countries-1": "Negara 1",
"Countries-2": "Negara 2",
"Countries-3": "Negara 3",
"Dairy": "Produk ternak perah",
"Days-of-the-Week-1": "Hari-hari dalam Seminggu 1",
"Days-of-the-Week-2": "Hari-hari dalam Seminggu 2",
"Dessert": "Makanan Penutup",
"Dining-Room": "Ruang Makan",
"Emergencies-1": "Kedaruratan 1",
"Emergencies-2": "Kedaruratan 2",
"Emergencies-3": "Kedaruratan 3",
"Emergencies-4": "Kedaruratan 4",
"Emergencies-5": "Kedaruratan 5",
"Family-1": "Keluarga 1",
"Family-2": "Keluarga 2",
"Family-3": "Keluarga 3",
"Family-4": "Keluarga 4",
"Fruit": "Buah",
"Going-to-the-Bank-1": "Pergi ke Bank 1",
"Going-to-the-Bank-2": "Pergi ke Bank 2",
"Going-to-the-Bank-3": "Pergi ke Bank 3",
"Going-to-the-Bank-4": "Pergi ke Bank 4",
"Grains": "Biji-bijian",
"Helper-Relationship-Facilitation": "Fasilitasi Hubungan Pembantu",
"House-Apartment-1": "Rumah/Apartemen 1",
"House-Apartment-2": "Rumah/Apartemen 2",
"Kitchen": "Dapur",
"Language-Learning-Facilitation-1": "Fasilitasi Pembelajaran Bahasa 1",
"Language-Learning-Facilitation-2": "Fasilitasi Pembelajaran Bahasa 2",
"Languages-1": "Bahasa 1",
"Languages-2": "Bahasa 2",
"Languages-3": "Bahasa 3",
"Languages-4": "Bahasa 4",
"Living-Room": "Ruang Tamu",
"Meals": "Makanan",
"Meat": "Daging",
"Meeting-and-Greeting-1": "Pertemuan dan Sapaan 1",
"Meeting-and-Greeting-2": "Pertemuan dan Sapaan 2",
"Months": "Bulan",
"Musical-Instruments-1": "Instrumen Musik 1",
"Musical-Instruments-2": "Instrumen Musik 2",
"Nature-1": "Alam 1",
"Nature-2": "Alam 2",
"Numbers-Cardinal-1": "Angka: Kardinal 1",
"Numbers-Cardinal-2": "Angka: Kardinal 2",
"Numbers-Cardinal-3": "Angka: Kardinal 3",
"Numbers-Cardinal-4": "Angka: Kardinal 4",
"Numbers-Ordinal": "Angka: Ordinal",
"Numbers-Other": "Angka: Lainnya",
"Office-1": "Kantor 1",
"Office-2": "Kantor 2",
"Parts-of-the-Body-1": "Bagian Tubuh 1",
"Parts-of-the-Body-2": "Bagian Tubuh 2",
"Personal-Pronouns": "Kata Ganti Orang",
"Places-1": "Tempat 1",
"Places-2": "Tempat 2",
"Polite-Conversation-1": "Percakapan Sopan 1",
"Polite-Conversation-2": "Percakapan Sopan 2",
"Polite-Conversation-3": "Percakapan Sopan 3",
"Possessive-Adjectives": "Kata Sifat Kepunyaan",
"Prepositions-1": "Preposisi 1",
"Prepositions-2": "Preposisi 2",
"Prepositions-3": "Preposisi 3",
"Prepositions-4": "Preposisi 4",
"Professions-1": "Profesi 1",
"Professions-2": "Profesi 2",
"Recreation-1": "Rekreasi 1",
"Recreation-2": "Rekreasi 2",
"Recreation-3": "Rekreasi 3",
"School-1": "Sekolah 1",
"School-2": "Sekolah 2",
"School-3": "Sekolah 3",
"Seafood": "Makanan Laut",
"Seasons": "Musim",
"Shapes": "Bentuk",
"Shopping-1": "Berbelanja 1",
"Shopping-2": "Berbelanja 2",
"Shopping-3": "Berbelanja 3",
"Shopping-4": "Berbelanja 4",
"Shopping-5": "Berbelanja 5",
"Shopping-Stores": "Berbelanja: Toko",
"Spices-Condiments": "Rempah/Bumbu",
"Taking-a-Taxi-1": "Naik Taksi 1",
"Taking-a-Taxi-2": "Naik Taksi 2",
"Taking-a-Taxi-3": "Naik Taksi 3",
"Time-1": "Waktu 1",
"Time-2": "Waktu 2",
"Translation-Facilitation": "Fasilitasi Terjemahan",
"Travel-1": "Perjalanan 1",
"Travel-2": "Perjalanan 2",
"Travel-3": "Perjalanan 3",
"Travel-4": "Perjalanan 4",
"Travel-5": "Perjalanan 5",
"Useful-Expressions": "Ungkapan yang Berguna",
"Vegetables": "Sayur-sayuran",
"Verbs-1": "Kata Kerja 1",
"Verbs-2": "Kata Kerja 2",
"Verbs-3": "Kata Kerja 3",
"Verbs-4": "Kata Kerja 4",
"Verbs-5": "Kata Kerja 5",
"Verbs-6": "Kata Kerja 6",
"Verbs-7": "Kata Kerja 7",
"Verbs-8": "Kata Kerja 8",
"Weather-1": "Cuaca 1",
"Weather-2": "Cuaca 2",
}
unitMap = {
"Pertemuan dan Sapaan": ["Meeting-and-Greeting-1",
"Meeting-and-Greeting-2"],
"Bantuan untuk Pembelajaran Bahasa": ["Communication-Facilitation-1",
"Communication-Facilitation-2",
"Communication-Facilitation-3",
"Communication-Facilitation-4",
"Communication-Facilitation-5",
"Communication-Facilitation-6",
"Communication-Facilitation-7"],
"Bantuan Lanjutan untuk Pembelajaran Bahasa": ["Helper-Relationship",
"Language-Learning-Facilitation-1",
"Language-Learning-Facilitation-2",
"Translation-Facilitation"],
"Percakapan Sopan": ["Polite-Conversation-1",
"Polite-Conversation-2",
"Polite-Conversation-3",
"Useful-Expressions"],
"Bentuk dan Warna": ["Shapes",
"Colors"],
"Pakaian": ["Clothing-1",
"Clothing-2",
"Clothing-3"],
"Berbelanja dan Toko": ["Shopping-Stores",
"Shopping-1",
"Shopping-2",
"Shopping-3",
"Shopping-4",
"Shopping-5"],
"Rumah dan Apartemen": ["House-Apartment-1",
"House-Apartment-2"],
"Ruangan di dalam Rumah": ["Living-Room",
"Dining-Room",
"Kitchen",
"Bathroom-1",
"Bathroom-2",
"Bedroom"],
"Keluarga": ["Family-1",
"Family-2",
"Family-3",
"Family-4"],
"Kantor dan Profesi": ["Office-1",
"Office-2",
"Professions-1",
"Professions-2"],
"Bagian Tubuh": ["Parts-of-the-Body-1",
"Parts-of-the-Body-2"],
"Kedaruratan": ["Emergencies-1",
"Emergencies-2",
"Emergencies-3",
"Emergencies-4",
"Emergencies-5"],
"Tempat dan Menanyakan Arah": ["Places-1",
"Places-2",
"Asking-for-Directions-1",
"Asking-for-Directions-2"],
"Sekolah": ["School-1",
"School-2",
"School-3"],
"Instrumen Musik": ["Musical-Instruments-1",
"Musical-Instruments-2"],
"Rekreasi": ["Recreation-1",
"Recreation-2",
"Recreation-3"],
"Alam": ["Nature-1",
"Nature-2"],
"Binatang": ["Animals-1",
"Animals-2"],
"Makanan 1": ["Meals",
"Beverages",
"Fruit",
"Vegetables",
"Grains"],
"Makanan 2": ["Dairy",
"Meat",
"Seafood",
"Spices-Condiments",
"Dessert"],
"Pergi ke Restoran": ["At-the-Restaurant-1",
"At-the-Restaurant-2",
"At-the-Restaurant-3",
"At-the-Restaurant-4",
"At-the-Restaurant-5"],
"Bahasa": ["Languages-1",
"Languages-2",
"Languages-3",
"Languages-4"],
"Negara": ["Continents",
"Countries-1",
"Countries-2",
"Countries-3"],
"Perjalanan": ["Travel-1",
"Travel-2",
"Travel-3",
"Travel-4",
"Travel-5"],
"Membeli Tiket": ["Buying-Tickets-1",
"Buying-Tickets-2",
"Buying-Tickets-3"],
"Naik Taksi": ["Taking-a-Taxi-1",
"Taking-a-Taxi-2",
"Taking-a-Taxi-3"],
"Menginap di Hotel": ["At-the-Hotel-1",
"At-the-Hotel-2",
"At-the-Hotel-3",
"At-the-Hotel-4"],
"Pergi ke Bank": ["Going-to-the-Bank-1",
"Going-to-the-Bank-2",
"Going-to-the-Bank-3",
"Going-to-the-Bank-4"],
"Angka": ["Numbers-Cardinal-1",
"Numbers-Cardinal-2",
"Numbers-Cardinal-3",
"Numbers-Cardinal-4",
"Numbers-Ordinal",
"Numbers-Other"],
"Hari-hari dalam Seminggu dan Waktu": ["Days-of-the-Week-1",
"Days-of-the-Week-2",
"Time-1",
"Time-2",
"Asking-the-Time"],
"Musim dan Cuaca": ["Months",
"Seasons",
"Weather-1",
"Weather-2"],
"Kata Ganti Orang dan Kata Sifat Kepunyaan": ["Personal-Pronouns",
"Possessive-Adjectives",
"Conjunctions"],
"Kata sifat dan Kata keterangan": ["Adjectives-1",
"Adjectives-2",
"Adjectives-3",
"Adverbs"],
"Kata Kerja": ["Verbs-1",
"Verbs-2",
"Verbs-3",
"Verbs-4",
"Verbs-5",
"Verbs-6",
"Verbs-7",
"Verbs-8"],
"Preposisi": ["Prepositions-1",
"Prepositions-2",
"Prepositions-3",
"Prepositions-4"],
}

baseText = """
Unit ini akan membantu Anda...

- mengingat kata-kata dan frasa-frasa yang terkait dengan topik ini
- belajar membaca dan menulis kata-kata dan frasa-frasa tersebut
- mengenal bunyi dan bisa mengucapkannya dengan benar

Mulailah dengan aktivitas seperti Language Comparison (Perbandingan Bahasa) dan Pronunciation Practice (Latihan Pengucapan) untuk membantu Anda menjadi terbiasa dengan materi ini.

Lanjutkan dengan aktivitas pilihan ganda dan menjodohkan yang berbasis wicara untuk meningkatkan pemahaman Anda atas kata-kata dan frasa-frasa yang diberikan.

Kemudian, lengkapi aktivitas menyimak dan mengetik untuk mempraktikkan produksi dan penulisan bahasa.

Akhirnya, lengkapi aktivitas penilaian pada akhir unit untuk menguji pengetahuan Anda atas kata-kata dan frasa-frasa yang diberikan."""

unitObjectives = {
"Pertemuan dan Sapaan": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan pertemuan dan sapaan." + "\n"+ baseText,
"Bantuan untuk Pembelajaran Bahasa": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan bantuan untuk pembelajaran bahasa." + "\n"+ baseText,
"Bantuan Lanjutan untuk Pembelajaran Bahasa": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan bantuan lanjutan untuk pembelajaran bahasa." + "\n"+ baseText,
"Percakapan Sopan": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan percakapan sopan." + "\n"+ baseText,
"Bentuk dan Warna": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan bentuk dan warna." + "\n"+ baseText,
"Pakaian": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan pakaian." + "\n"+ baseText,
"Berbelanja dan Toko": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan berbelanja dan toko." + "\n"+ baseText,
"Rumah dan Apartemen": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan rumah dan apartemen." + "\n"+ baseText,
"Ruangan di dalam Rumah": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan ruangan di dalam rumah." + "\n"+ baseText,
"Keluarga": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan keluarga." + "\n"+ baseText,
"Kantor dan Profesi": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan kantor dan profesi." + "\n"+ baseText,
"Bagian Tubuh": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan bagian tubuh." + "\n"+ baseText,
"Kedaruratan": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan kedaruratan." + "\n"+ baseText,
"Tempat dan Menanyakan Arah": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan tempat dan menanyakan arah." + "\n"+ baseText,
"Sekolah": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan sekolah." + "\n"+ baseText,
"Instrumen Musik": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan instrumen musik." + "\n"+ baseText,
"Rekreasi": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan rekreasi." + "\n"+ baseText,
"Alam": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan alam." + "\n"+ baseText,
"Binatang": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan binatang." + "\n"+ baseText,
"Makanan 1": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan makanan." + "\n"+ baseText,
"Makanan 2": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan makanan." + "\n"+ baseText,
"Pergi ke Restoran": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan pergi ke restoran." + "\n"+ baseText,
"Bahasa": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan bahasa." + "\n"+ baseText,
"Negara": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan negara." + "\n"+ baseText,
"Perjalanan": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan perjalanan." + "\n"+ baseText,
"Membeli Tiket": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan membeli tiket." + "\n"+ baseText,
"Naik Taksi": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan naik taksi." + "\n"+ baseText,
"Menginap di Hotel": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan menginap di hotel." + "\n"+ baseText,
"Pergi ke Bank": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan pergi ke bank." + "\n"+ baseText,
"Angka": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan angka." + "\n"+ baseText,
"Hari-hari dalam Seminggu dan Waktu": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan hari-hari dalam seminggu dan waktu." + "\n"+ baseText,
"Musim dan Cuaca": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan musim dan cuaca." + "\n"+ baseText,
"Kata Ganti Orang dan Kata Sifat Kepunyaan": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan kata ganti orang dan kata sifat kepunyaan." + "\n"+ baseText,
"Kata sifat dan Kata keterangan": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan kata sifat dan kata keterangan." + "\n"+ baseText,
"Kata Kerja": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan kata kerja." + "\n"+ baseText,
"Preposisi": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan preposisi." + "\n"+ baseText,
}
lessonOrder = unitMap
languageDict = [
    ["x for Indonesian Speakers", "English"],
]
projectName = "supplementalVocabCoursesESLINDid"
isESLTrue = True


def createSVCConfiguration():
    """
    takes the above information and builds a course object for the rest of the scripts

    :return: a filled out course object
    """
    configObject = courseConfiguration()
    configObject.projectName = projectName
    configObject.unitNameList = unitNameList
    configObject.languageDict = languageDict
    configObject.unitMap = unitMap
    configObject.unitObjectives = unitObjectives
    configObject.lessonOrder = lessonOrder
    configObject.unitNumbers = configObject.createUnitNumbers(unitNameList)
    configObject.lessonToList = lessonNameToListNameMap
    configObject.isESLTrue = isESLTrue
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(unitNameList)

    return configObject