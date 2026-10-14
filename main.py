import dataclasses
from string import Template


@dataclasses.dataclass
class NtcTable:
    temperature: int
    resistance: int


@dataclasses.dataclass
class NewNtcTable:
    temperature: int
    acp: int


ntcTable = [
    NtcTable(-34, 55400),
    NtcTable(-33, 51760),
    NtcTable(-32, 48100),
    NtcTable(-31, 46700),
    NtcTable(-30, 45300),
    NtcTable(-29, 41200),
    NtcTable(-28, 39300),
    NtcTable(-27, 38200),
    NtcTable(-26, 34800),
    NtcTable(-25, 33600),
    NtcTable(-24, 31300),
    NtcTable(-23, 29700),
    NtcTable(-22, 28200),
    NtcTable(-21, 26400),
    NtcTable(-20, 24900),
    NtcTable(-19, 23900),
    NtcTable(-18, 22800),
    NtcTable(-17, 21400),
    NtcTable(-16, 20600),
    NtcTable(-15, 18760),
    NtcTable(-14, 17910),
    NtcTable(-13, 17080),
    NtcTable(-12, 16700),
    NtcTable(-11, 15705),
    NtcTable(-10, 14710),
    NtcTable(-9, 13900),
    NtcTable(-8, 13310),
    NtcTable(-7, 12780),
    NtcTable(-6, 12300),
    NtcTable(-5, 11590),
    NtcTable(-4, 11060),
    NtcTable(-3, 10280),
    NtcTable(-2, 10000),
    NtcTable(-1, 9360),
    NtcTable(0, 9100),
    NtcTable(1, 8655),
    NtcTable(2, 8210),
    NtcTable(3, 7740),
    NtcTable(4, 7400),
    NtcTable(5, 7000),
    NtcTable(6, 6750),
    NtcTable(7, 6500),
    NtcTable(8, 6180),
    NtcTable(9, 5830),
    NtcTable(10, 5630),
    NtcTable(11, 5260),
    NtcTable(12, 4970),
    NtcTable(13, 4735),
    NtcTable(14, 4500),
    NtcTable(15, 4340),
    NtcTable(16, 4170),
    NtcTable(17, 3980),
    NtcTable(18, 3780),
    NtcTable(19, 3680),
    NtcTable(20, 3450),
    NtcTable(21, 3270),
    NtcTable(22, 3140),
    NtcTable(23, 3010),
    NtcTable(24, 2890),
    NtcTable(25, 2760),
    NtcTable(26, 2640),
    NtcTable(27, 2530),
    NtcTable(28, 2410),
    NtcTable(29, 2300),
    NtcTable(30, 2190),
    NtcTable(31, 2100),
    NtcTable(32, 2010),
    NtcTable(33, 1949),
    NtcTable(34, 1870),
    NtcTable(35, 1790),
    NtcTable(36, 1718),
    NtcTable(37, 1642),
    NtcTable(38, 1580),
    NtcTable(39, 1519),
    NtcTable(40, 1451),
    NtcTable(41, 1396),
    NtcTable(42, 1343),
    NtcTable(43, 1291),
    NtcTable(44, 1243),
    NtcTable(45, 1195),
    NtcTable(46, 1147),
    NtcTable(47, 1103),
    NtcTable(48, 1063),
    NtcTable(49, 1022),
    NtcTable(50, 982),
    NtcTable(51, 942),
    NtcTable(52, 902),
    NtcTable(53, 870),
    NtcTable(54, 839),
    NtcTable(55, 808),
    NtcTable(56, 775),
    NtcTable(57, 746),
    NtcTable(58, 720),
    NtcTable(59, 696),
    NtcTable(60, 673),
    NtcTable(61, 649),
    NtcTable(62, 624),
    NtcTable(63, 601),
    NtcTable(64, 579),
    NtcTable(65, 557),
    NtcTable(66, 537),
    NtcTable(67, 518),
    NtcTable(68, 500),
    NtcTable(69, 482),
    NtcTable(70, 464),
    NtcTable(71, 448),
    NtcTable(72, 433),
    NtcTable(73, 419),
    NtcTable(74, 406),
    NtcTable(75, 394),
    NtcTable(76, 382),
    NtcTable(77, 369),
    NtcTable(78, 357),
    NtcTable(79, 345),
    NtcTable(80, 333),
    NtcTable(81, 322),
    NtcTable(82, 311),
    NtcTable(83, 300),
    NtcTable(84, 290),
    NtcTable(85, 281),
    NtcTable(86, 272),
    NtcTable(87, 263),
    NtcTable(88, 255),
    NtcTable(89, 246),
    NtcTable(90, 238),
    NtcTable(91, 230),
    NtcTable(92, 222),
    NtcTable(93, 215),
    NtcTable(94, 208),
    NtcTable(95, 201),
    NtcTable(96, 195),
    NtcTable(97, 189),
    NtcTable(98, 183),
    NtcTable(99, 178),
    NtcTable(100, 174),
]

newNtcTable: list[NewNtcTable] = []

RESISTOR_FROM_SENSOR = 2000
MAX_ACP = 1023

for index in range(len(ntcTable) - 1):
    r_high = ntcTable[index].resistance
    r_low = ntcTable[index + 1].resistance
    temperature = ntcTable[index].temperature

    best_acp = None
    for acp in range(MAX_ACP + 1):
        if acp == MAX_ACP:
            resistance = float("inf")
        else:
            resistance = RESISTOR_FROM_SENSOR * acp / (MAX_ACP - acp)

        if r_low <= resistance <= r_high:
            best_acp = acp
            break

    if best_acp is not None:
        newNtcTable.append(NewNtcTable(temperature, best_acp))


print("=======END======")

final_str = ""
start_method = "static const NtcPoint ntcTable[] PROGMEM = {"
final_str += start_method
for index, n in enumerate(newNtcTable):
    fmt_str = "{$temperature, $acp}"
    if index + 1 != len(newNtcTable):
        fmt_str += ","
    final_str += Template(fmt_str).substitute(
            temperature=n.temperature, acp=n.acp
    ) + '\n'

end = "};"
final_str += end
print(final_str)
with open("table_result.txt", "w") as f:
    f.write(final_str)
