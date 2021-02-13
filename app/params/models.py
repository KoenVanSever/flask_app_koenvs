from app import db
from pathlib import Path

# ! Parameter file mapping bottom of document !


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


def process_2b(lsb, msb):
    """Merge two bytes into bigger integer

    Args:
        lsb (int): least significant byte
        msb (int): most siginificant byte

    Returns:
        int: value up to 65535
    """
    return msb * 256 + lsb


def split_2b(num):
    """Split a 16 bit in 2x 8 bit

    Args:
        num (int): number below or equal to 65535

    Returns:
        list (2x string): split in bytes (string format)
    """
    lsb = num % 256
    msb = num // 256
    return [str(lsb), str(msb)]


class Params(Base):
    __tablename__ = "parameters_files"

    # Text
    csv_name = db.Column("csv_name", db.String(128), unique=True, nullable=False)
    short_name = db.Column("short_name", db.String(64), nullable=False)
    light_family = db.Column("light_family", db.String(32))

    # Bytes
    byte_128 = db.Column("byte_128", db.SmallInteger, nullable=False)
    byte_129 = db.Column("byte_129", db.SmallInteger, nullable=False)
    byte_130 = db.Column("byte_130", db.SmallInteger, nullable=False)
    byte_131 = db.Column("byte_131", db.SmallInteger, nullable=False)
    byte_132 = db.Column("byte_132", db.SmallInteger, nullable=False)
    byte_133 = db.Column("byte_133", db.SmallInteger, nullable=False)
    byte_134 = db.Column("byte_134", db.SmallInteger, nullable=False)
    byte_135 = db.Column("byte_135", db.SmallInteger, nullable=False)
    byte_136 = db.Column("byte_136", db.SmallInteger, default=0, nullable=False)
    byte_137_138 = db.Column("byte_137/138", db.SmallInteger, nullable=False)
    byte_139 = db.Column("byte_139", db.SmallInteger, nullable=False)
    byte_140 = db.Column("byte_140", db.SmallInteger, default=10, nullable=False)
    byte_141 = db.Column("byte_141", db.SmallInteger, default=130, nullable=False)
    byte_142 = db.Column("byte_142", db.SmallInteger, default=180, nullable=False)
    byte_143 = db.Column("byte_143", db.SmallInteger, default=156, nullable=False)
    byte_144 = db.Column("byte_144", db.SmallInteger, default=1, nullable=False)
    byte_145 = db.Column("byte_145", db.SmallInteger, nullable=False)
    byte_146 = db.Column("byte_146", db.SmallInteger, default=0, nullable=False)
    byte_147_148 = db.Column("byte_147/148", db.SmallInteger, nullable=False)
    byte_149_150 = db.Column("byte_149/150", db.SmallInteger, nullable=False)
    byte_151_152 = db.Column("byte_151/152", db.SmallInteger, nullable=False)
    byte_153_154 = db.Column("byte_153/154", db.SmallInteger, nullable=False)
    byte_155_156 = db.Column("byte_155/156", db.SmallInteger, nullable=False)
    byte_157_158 = db.Column("byte_157/158", db.SmallInteger, nullable=False)
    byte_159_160 = db.Column("byte_159/160", db.SmallInteger, nullable=False)
    byte_161_162 = db.Column("byte_161/162", db.SmallInteger, nullable=False)
    byte_163 = db.Column("byte_163", db.SmallInteger, nullable=False)
    byte_164 = db.Column("byte_164", db.SmallInteger, nullable=False)
    byte_165 = db.Column("byte_165", db.SmallInteger, nullable=False)
    byte_166 = db.Column("byte_166", db.SmallInteger, nullable=False)
    byte_167 = db.Column("byte_167", db.SmallInteger, nullable=False)
    byte_168 = db.Column("byte_168", db.SmallInteger, nullable=False)
    byte_169_170 = db.Column("byte_169/170", db.SmallInteger, nullable=False)
    byte_171 = db.Column("byte_171", db.SmallInteger, nullable=False)
    byte_172 = db.Column("byte_172", db.SmallInteger, nullable=False)
    byte_173 = db.Column("byte_173", db.SmallInteger, nullable=False)
    byte_174 = db.Column("byte_174", db.SmallInteger, nullable=False)
    byte_175_176 = db.Column("byte_175/176", db.SmallInteger, nullable=False)
    byte_177_178 = db.Column("byte_177/178", db.SmallInteger, nullable=False)
    byte_179_180 = db.Column("byte_179/180", db.SmallInteger, nullable=False)
    byte_181_182 = db.Column("byte_181/182", db.SmallInteger, nullable=False)
    byte_183_184 = db.Column("byte_183/184", db.SmallInteger, nullable=False)
    byte_185_186 = db.Column("byte_185/186", db.SmallInteger, nullable=False)
    byte_187_188 = db.Column("byte_187/188", db.SmallInteger, nullable=False)
    byte_189_190 = db.Column("byte_189/190", db.SmallInteger, nullable=False)
    byte_191_192 = db.Column("byte_191/192", db.SmallInteger, nullable=False)
    byte_193_194 = db.Column("byte_193/194", db.SmallInteger, nullable=False)
    byte_195_196 = db.Column("byte_195/196", db.SmallInteger, nullable=False)
    byte_197_198 = db.Column("byte_197/198", db.SmallInteger, nullable=False)
    byte_199_200 = db.Column("byte_199/200", db.SmallInteger, nullable=False)
    byte_201 = db.Column("byte_201", db.SmallInteger, default=18, nullable=False)
    byte_202_203 = db.Column("byte_202/203", db.SmallInteger, default=300, nullable=False)
    byte_204_205 = db.Column("byte_204/205", db.SmallInteger, default=610, nullable=False)
    byte_206 = db.Column("byte_206", db.SmallInteger, nullable=False)
    byte_207 = db.Column("byte_207", db.SmallInteger, nullable=False)
    byte_208_209 = db.Column("byte_208/209", db.SmallInteger, nullable=False)
    byte_210_211 = db.Column("byte_210/211", db.SmallInteger, nullable=False)
    byte_212 = db.Column("byte_212", db.SmallInteger, nullable=False)
    byte_213 = db.Column("byte_213", db.SmallInteger, nullable=False)
    byte_214 = db.Column("byte_214", db.SmallInteger, nullable=False)
    byte_215 = db.Column("byte_215", db.SmallInteger, nullable=False)

    @classmethod
    def upload_file(cls, path, delim=";", category=None):
        """
        Args:
            path (Path): Pathlib object from the correct filepath for this file you want to parse
            delim (str): Delimiter used in csv-file. Defaults to ";"
            category (str, optional): The category of lights in which these row falls. Defaults to None.

        Raises:
            AttributeError: File is not of correct structure, data must be on first line and must be 257 fields long
        """
        with open(path) as file:
            line_1 = file.readline()
            data = line_1.split(delim)
            if isinstance(data, list) and len(data) == 257:
                temp = cls()  # make object of class
                temp.csv_name = path.name
                temp.short_name = data.pop(0)
                if category:
                    temp.category = category
                byte_data_map = dict(zip(range(256), map(int, data)))
                temp._process_byte_data_map(byte_data_map)
                return temp
            else:
                raise AttributeError("Uploaded parameter file is not the correct length")

    def export_csv(self, delimiter=";", **kwargs):
        """
        Generate a csv file from the SQL parameters in the database

        Args:
            delimiter (str, optional): delimiter used for the csv file. Defaults to ";".
        Kwargs:
            filename: output filename - if not used, use csv_name inside the SQL DB
        """
        filename = kwargs.pop("filename", self.csv_name)
        data_map = self._generate_byte_data_map()
        vals = list(data_map.values())
        param = [self.short_name] + vals
        line = delimiter.join(param) + "\n"
        with open(Path("app", "temporary", filename), "w") as file:
            file.write(line)

    @property
    def flux_summ(self):
        fluxes = [self.byte_163, self.byte_164, self.byte_165, self.byte_166, self.byte_167, self.byte_168]
        if all([x == fluxes[0] for x in fluxes]):
            return fluxes[0]
        else:
            return "Vary"

    def _generate_byte_data_map(self):
        data_map = dict(zip(range(256), ["255"] * 256))
        data_map[128] = str(self.byte_128)
        data_map[129] = str(self.byte_129)
        data_map[130] = str(self.byte_130)
        data_map[131] = str(self.byte_131)
        data_map[132] = str(self.byte_132)
        data_map[133] = str(self.byte_133)
        data_map[134] = str(self.byte_134)
        data_map[135] = str(self.byte_135)
        data_map[136] = str(self.byte_136)
        data_map[137], data_map[138] = split_2b(self.byte_137_138)
        data_map[139] = str(self.byte_139)
        data_map[140] = str(self.byte_140)
        data_map[141] = str(self.byte_141)
        data_map[142] = str(self.byte_142)
        data_map[143] = str(self.byte_143)
        data_map[144] = str(self.byte_144)
        data_map[145] = str(self.byte_145)
        data_map[146] = str(self.byte_146)
        data_map[147], data_map[148] = split_2b(self.byte_147_148)
        data_map[149], data_map[150] = split_2b(self.byte_149_150)
        data_map[151], data_map[152] = split_2b(self.byte_151_152)
        data_map[153], data_map[154] = split_2b(self.byte_153_154)
        data_map[155], data_map[156] = split_2b(self.byte_155_156)
        data_map[157], data_map[158] = split_2b(self.byte_157_158)
        data_map[159], data_map[160] = split_2b(self.byte_159_160)
        data_map[161], data_map[162] = split_2b(self.byte_161_162)
        data_map[163] = str(self.byte_163)
        data_map[164] = str(self.byte_164)
        data_map[165] = str(self.byte_165)
        data_map[166] = str(self.byte_166)
        data_map[167] = str(self.byte_167)
        data_map[168] = str(self.byte_168)
        data_map[169], data_map[170] = split_2b(self.byte_169_170)
        data_map[171] = str(self.byte_171)
        data_map[172] = str(self.byte_172)
        data_map[173] = str(self.byte_173)
        data_map[174] = str(self.byte_174)
        data_map[175], data_map[176] = split_2b(self.byte_175_176)
        data_map[177], data_map[178] = split_2b(self.byte_177_178)
        data_map[179], data_map[180] = split_2b(self.byte_179_180)
        data_map[181], data_map[182] = split_2b(self.byte_181_182)
        data_map[183], data_map[184] = split_2b(self.byte_183_184)
        data_map[185], data_map[186] = split_2b(self.byte_185_186)
        data_map[187], data_map[188] = split_2b(self.byte_187_188)
        data_map[189], data_map[190] = split_2b(self.byte_189_190)
        data_map[191], data_map[192] = split_2b(self.byte_191_192)
        data_map[193], data_map[194] = split_2b(self.byte_193_194)
        data_map[195], data_map[196] = split_2b(self.byte_195_196)
        data_map[197], data_map[198] = split_2b(self.byte_197_198)
        data_map[199], data_map[200] = split_2b(self.byte_199_200)
        data_map[201] = str(self.byte_201)
        data_map[202], data_map[203] = split_2b(self.byte_202_203)
        data_map[204], data_map[205] = split_2b(self.byte_204_205)
        data_map[206] = str(self.byte_206)
        data_map[207] = str(self.byte_207)
        data_map[208], data_map[209] = split_2b(self.byte_208_209)
        data_map[210], data_map[211] = split_2b(self.byte_210_211)
        data_map[212] = str(self.byte_212)
        data_map[213] = str(self.byte_213)
        data_map[214] = str(self.byte_214)
        data_map[215] = str(self.byte_215)
        return data_map

    def _process_byte_data_map(self, data_map):
        self.byte_128 = data_map[128]
        self.byte_129 = data_map[129]
        self.byte_130 = data_map[130]
        self.byte_131 = data_map[131]
        self.byte_132 = data_map[132]
        self.byte_133 = data_map[133]
        self.byte_134 = data_map[134]
        self.byte_135 = data_map[135]
        self.byte_136 = data_map[136]
        self.byte_137_138 = process_2b(data_map[137], data_map[138])
        self.byte_139 = data_map[139]
        self.byte_140 = data_map[140]
        self.byte_141 = data_map[141]
        self.byte_142 = data_map[142]
        self.byte_143 = data_map[143]
        self.byte_144 = data_map[144]
        self.byte_145 = data_map[145]
        self.byte_146 = data_map[146]
        self.byte_147_148 = process_2b(data_map[147], data_map[148])
        self.byte_149_150 = process_2b(data_map[149], data_map[150])
        self.byte_151_152 = process_2b(data_map[151], data_map[152])
        self.byte_153_154 = process_2b(data_map[153], data_map[154])
        self.byte_155_156 = process_2b(data_map[155], data_map[156])
        self.byte_157_158 = process_2b(data_map[157], data_map[158])
        self.byte_159_160 = process_2b(data_map[159], data_map[160])
        self.byte_161_162 = process_2b(data_map[161], data_map[162])
        self.byte_163 = data_map[163]
        self.byte_164 = data_map[164]
        self.byte_165 = data_map[165]
        self.byte_166 = data_map[166]
        self.byte_167 = data_map[167]
        self.byte_168 = data_map[168]
        self.byte_169_170 = process_2b(data_map[169], data_map[170])
        self.byte_171 = data_map[171]
        self.byte_172 = data_map[172]
        self.byte_173 = data_map[173]
        self.byte_174 = data_map[174]
        self.byte_175_176 = process_2b(data_map[175], data_map[176])
        self.byte_177_178 = process_2b(data_map[177], data_map[178])
        self.byte_179_180 = process_2b(data_map[179], data_map[180])
        self.byte_181_182 = process_2b(data_map[181], data_map[182])
        self.byte_183_184 = process_2b(data_map[183], data_map[184])
        self.byte_185_186 = process_2b(data_map[185], data_map[186])
        self.byte_187_188 = process_2b(data_map[187], data_map[188])
        self.byte_189_190 = process_2b(data_map[189], data_map[190])
        self.byte_191_192 = process_2b(data_map[191], data_map[192])
        self.byte_193_194 = process_2b(data_map[193], data_map[194])
        self.byte_195_196 = process_2b(data_map[195], data_map[196])
        self.byte_197_198 = process_2b(data_map[197], data_map[198])
        self.byte_199_200 = process_2b(data_map[199], data_map[200])
        self.byte_201 = data_map[201]
        self.byte_202_203 = process_2b(data_map[202], data_map[203])
        self.byte_204_205 = process_2b(data_map[204], data_map[205])
        self.byte_206 = data_map[206]
        self.byte_207 = data_map[207]
        self.byte_208_209 = process_2b(data_map[208], data_map[209])
        self.byte_210_211 = process_2b(data_map[210], data_map[211])
        self.byte_212 = data_map[212]
        self.byte_213 = data_map[213]
        self.byte_214 = data_map[214]
        self.byte_215 = data_map[215]

    def export_dict(self):
        ret_dict = {}
        ret_dict["Nominal Current (mA)"] = (self.byte_137_138, "led-col")
        ret_dict["Nominal Voltage (100 mV)"] = (self.byte_139, "led-col")
        ret_dict["Nominal Voltage (10 mV)"] = (self.byte_210_211, "led-col")
        ret_dict["Minimum Linear Dimming"] = (self.byte_202_203, "led-col")
        ret_dict["Digital Dimming Frequency"] = (self.byte_204_205, "led-col")
        ret_dict["Number of LEDs"] = (self.byte_145, "led-col")
        ret_dict["LED revision"] = (self.byte_146, "led-col")
        ret_dict["Load Type"] = (self.byte_212, "led-col")

        ret_dict["Dimming Curve 1400 mA"] = (self.byte_147_148, "dc-col")
        ret_dict["Dimming Curve 2800 mA"] = (self.byte_149_150, "dc-col")
        ret_dict["Dimming Curve 3400 mA"] = (self.byte_151_152, "dc-col")
        ret_dict["Dimming Curve 4100 mA"] = (self.byte_153_154, "dc-col")
        ret_dict["Dimming Curve 4800 mA"] = (self.byte_155_156, "dc-col")
        ret_dict["Dimming Curve 5200 mA"] = (self.byte_157_158, "dc-col")
        ret_dict["Dimming Curve 5500 mA"] = (self.byte_159_160, "dc-col")
        ret_dict["Dimming Curve 6600 mA"] = (self.byte_161_162, "dc-col")

        ret_dict["Flux Compensation (-25 °C)"] = (self.byte_163, "flux-col")
        ret_dict["Flux Compensation (0 °C)"] = (self.byte_164, "flux-col")
        ret_dict["Flux Compensation (25 °C)"] = (self.byte_165, "flux-col")
        ret_dict["Flux Compensation (50 °C)"] = (self.byte_166, "flux-col")
        ret_dict["Flux Compensation (75 °C)"] = (self.byte_167, "flux-col")
        ret_dict["Flux Compensation (Max °C)"] = (self.byte_168, "flux-col")

        ret_dict["AK Power 1 Window"] = (self.byte_213, "ak-col")
        ret_dict["AK Power 2 Window"] = (self.byte_214, "ak-col")

        ret_dict["Vf Short Threshold Fast"] = (self.byte_206, "led-ext-col")
        ret_dict["Vf Short Threshold Slow"] = (self.byte_207, "led-ext-col")
        ret_dict["Minimum On Time"] = (self.byte_208_209, "led-ext-col")
        ret_dict["Dual Monitoring"] = (self.byte_215, "led-ext-col")

        ret_dict["Release Year"] = (self.byte_128, "rel-col")
        ret_dict["Release Week"] = (self.byte_129, "rel-col")
        ret_dict["Release Version"] = (self.byte_130, "rel-col")
        ret_dict["Release Not Used"] = (self.byte_131, "rel-col")

        ret_dict["Inverse Release Year"] = (self.byte_132, "rel-col")
        ret_dict["Inverse Release Week"] = (self.byte_132, "rel-col")
        ret_dict["Inverse Release Version "] = (self.byte_134, "rel-col")
        ret_dict["Inverse Release Not Used"] = (self.byte_135, "rel-col")

        ret_dict["Programming Date Year"] = (self.byte_171, "prog-col")
        ret_dict["Programming Date Month"] = (self.byte_172, "prog-col")
        ret_dict["Programming Date Day"] = (self.byte_173, "prog-col")
        ret_dict["Programming Date Hour"] = (self.byte_174, "prog-col")

        ret_dict["LED PWM Level 1"] = (self.byte_175_176, "led-var-col")
        ret_dict["LED PWM Level 2"] = (self.byte_177_178, "led-var-col")
        ret_dict["LED PWM Level 3"] = (self.byte_179_180, "led-var-col")
        ret_dict["LED PWM Level 4"] = (self.byte_181_182, "led-var-col")
        ret_dict["LED PWM Level 5"] = (self.byte_183_184, "led-var-col")
        ret_dict["LED PWM Level 6"] = (self.byte_185_186, "led-var-col")
        ret_dict["LED Voltage Level 1"] = (self.byte_187_188, "led-var-col")
        ret_dict["LED Voltage Level 2"] = (self.byte_189_190, "led-var-col")
        ret_dict["LED Voltage Level 3"] = (self.byte_191_192, "led-var-col")
        ret_dict["LED Voltage Level 4"] = (self.byte_193_194, "led-var-col")
        ret_dict["LED Voltage Level 5"] = (self.byte_195_196, "led-var-col")
        ret_dict["LED Voltage Level 6"] = (self.byte_197_198, "led-var-col")

        ret_dict["Thermal Resistance"] = (self.byte_140, "random-col")
        ret_dict["Max Junction Temperature (°C)"] = (self.byte_141, "random-col")
        ret_dict["Type"] = (self.byte_136, "random-col")
        ret_dict["Flux bin information"] = (self.byte_142, "random-col")
        ret_dict["Color"] = (self.byte_143, "random-col")
        ret_dict["Fitting Type"] = (self.byte_144, "random-col")
        ret_dict["Reserved Version"] = (self.byte_169_170, "random-col")
        ret_dict["CRC (based on 128-198)"] = (self.byte_199_200, "random-col")
        ret_dict["Length Block 1"] = (self.byte_201, "random-col")

        return ret_dict

    def update_with_dict(self, immutabledict):
        self.csv_name = immutabledict["csv_name"]
        self.short_name = immutabledict["short_name"]
        self.light_family = immutabledict["light_family"]

        self.byte_137_138 = immutabledict["Nominal Current (mA)"]
        self.byte_139 = immutabledict["Nominal Voltage (100 mV)"]
        self.byte_210_211 = immutabledict["Nominal Voltage (10 mV)"]
        self.byte_202_203 = immutabledict["Minimum Linear Dimming"]
        self.byte_204_205 = immutabledict["Digital Dimming Frequency"]
        self.byte_145 = immutabledict["Number of LEDs"]
        self.byte_146 = immutabledict["LED revision"]
        self.byte_212 = immutabledict["Load Type"]

        self.byte_147_148 = immutabledict["Dimming Curve 1400 mA"]
        self.byte_149_150 = immutabledict["Dimming Curve 2800 mA"]
        self.byte_151_152 = immutabledict["Dimming Curve 3400 mA"]
        self.byte_153_154 = immutabledict["Dimming Curve 4100 mA"]
        self.byte_155_156 = immutabledict["Dimming Curve 4800 mA"]
        self.byte_157_158 = immutabledict["Dimming Curve 5200 mA"]
        self.byte_159_160 = immutabledict["Dimming Curve 5500 mA"]
        self.byte_161_162 = immutabledict["Dimming Curve 6600 mA"]

        self.byte_163 = immutabledict["Flux Compensation (-25 °C)"]
        self.byte_164 = immutabledict["Flux Compensation (0 °C)"]
        self.byte_165 = immutabledict["Flux Compensation (25 °C)"]
        self.byte_166 = immutabledict["Flux Compensation (50 °C)"]
        self.byte_167 = immutabledict["Flux Compensation (75 °C)"]
        self.byte_168 = immutabledict["Flux Compensation (Max °C)"]

        self.byte_213 = immutabledict["AK Power 1 Window"]
        self.byte_214 = immutabledict["AK Power 2 Window"]

        self.byte_206 = immutabledict["Vf Short Threshold Fast"]
        self.byte_207 = immutabledict["Vf Short Threshold Slow"]
        self.byte_208_209 = immutabledict["Minimum On Time"]
        self.byte_215 = immutabledict["Dual Monitoring"]

        self.byte_128 = immutabledict["Release Year"]
        self.byte_129 = immutabledict["Release Week"]
        self.byte_130 = immutabledict["Release Version"]
        self.byte_131 = immutabledict["Release Not Used"]

        self.byte_132 = immutabledict["Inverse Release Year"]
        self.byte_133 = immutabledict["Inverse Release Week"]
        self.byte_134 = immutabledict["Inverse Release Version "]
        self.byte_135 = immutabledict["Inverse Release Not Used"]

        self.byte_171 = immutabledict["Programming Date Year"]
        self.byte_172 = immutabledict["Programming Date Month"]
        self.byte_173 = immutabledict["Programming Date Day"]
        self.byte_174 = immutabledict["Programming Date Hour"]

        self.byte_175_176 = immutabledict["LED PWM Level 1"]
        self.byte_177_178 = immutabledict["LED PWM Level 2"]
        self.byte_179_180 = immutabledict["LED PWM Level 3"]
        self.byte_181_182 = immutabledict["LED PWM Level 4"]
        self.byte_183_184 = immutabledict["LED PWM Level 5"]
        self.byte_185_186 = immutabledict["LED PWM Level 6"]
        self.byte_187_188 = immutabledict["LED Voltage Level 1"]
        self.byte_189_190 = immutabledict["LED Voltage Level 2"]
        self.byte_191_192 = immutabledict["LED Voltage Level 3"]
        self.byte_193_194 = immutabledict["LED Voltage Level 4"]
        self.byte_195_196 = immutabledict["LED Voltage Level 5"]
        self.byte_197_198 = immutabledict["LED Voltage Level 6"]

        self.byte_140 = immutabledict["Thermal Resistance"]
        self.byte_141 = immutabledict["Max Junction Temperature (°C)"]
        self.byte_136 = immutabledict["Type"]
        self.byte_142 = immutabledict["Flux bin information"]
        self.byte_143 = immutabledict["Color"]
        self.byte_144 = immutabledict["Fitting Type"]
        self.byte_169_170 = immutabledict["Reserved Version"]
        self.byte_199_200 = immutabledict["CRC (based on 128-198)"]
        self.byte_201 = immutabledict["Length Block 1"]

        return None


# -------------------------
# -- Parameter File Mapping
# -------------------------
# * byte_0-127      - Unused (default 255)
# * byte_128        - Release Year                  - 1b
# * byte_129        - Release Week                  - 1b
# * byte_130        - Release Version               - 1b
# * byte_131        - Release Not Used              - 1b
# * byte_132        - Inverse Release Year          - 1b
# * byte_132        - Inverse Release Week          - 1b
# * byte_134        - Inverse Release Version       - 1b
# * byte_135        - Inverse Release Not Used      - 1b
# * byte_136        - Type                          - 1b
# * byte_137/138    - Nominal Current (mA)          - 2b
# * byte_139        - Nominal Voltage (100 mV)      - 1b
# * byte_140        - Thermal Resistance            - 1b
# * byte_141        - Max Junction Temperature (°C) - 1b
# * byte_142        - Flux bin information          - 1b
# * byte_143        - Color                         - 1b
# * byte_144        - Fitting Type                  - 1b
# * byte_145        - Number of LEDs                - 1b
# * byte_146        - LED revision                  - 1b
# * byte_147/148    - Dimming Curve 1400 mA         - 2b
# * byte_149/150    - Dimming Curve 2800 mA         - 2b
# * byte_151/152    - Dimming Curve 3400 mA         - 2b
# * byte_153/154    - Dimming Curve 4100 mA         - 2b
# * byte_155/156    - Dimming Curve 4800 mA         - 2b
# * byte_157/158    - Dimming Curve 5200 mA         - 2b
# * byte_159/160    - Dimming Curve 5500 mA         - 2b
# * byte_161/162    - Dimming Curve 6600 mA         - 2b
# * byte_163        - Flux Compensation (-25 °C)    - 1b
# * byte_164        - Flux Compensation (0 °C)      - 1b
# * byte_165        - Flux Compensation (25 °C)     - 1b
# * byte_166        - Flux Compensation (50 °C)     - 1b
# * byte_167        - Flux Compensation (75 °C)     - 1b
# * byte_168        - Flux Compensation (Max °C)    - 1b
# * byte_169/170    - Reserved Version              - 2b
# * byte_171        - Programming Date Year         - 1b
# * byte_172        - Programming Date Month        - 1b
# * byte_173        - Programming Date Day          - 1b
# * byte_174        - Programming Date Hour         - 1b
# * byte_175/176    - LED PWM Level 1               - 2b
# * byte_177/178    - LED PWM Level 2               - 2b
# * byte_179/180    - LED PWM Level 3               - 2b
# * byte_181/182    - LED PWM Level 4               - 2b
# * byte_183/184    - LED PWM Level 5               - 2b
# * byte_185/186    - LED PWM Level 6               - 2b
# * byte_187/188    - LED Voltage Level 1           - 2b
# * byte_189/190    - LED Voltage Level 2           - 2b
# * byte_191/192    - LED Voltage Level 3           - 2b
# * byte_193/194    - LED Voltage Level 4           - 2b
# * byte_195/196    - LED Voltage Level 5           - 2b
# * byte_197/198    - LED Voltage Level 6           - 2b
# * byte_199/200    - CRC (based on 128-198)        - 2b
# * byte_201        - Length Block 1                - 1b
# * byte_202/203    - Minimum Linear Dimming        - 2b
# * byte_204/205    - Digital Dimming Frequency     - 2b
# * byte_206        - Vf Short Threshold Fast       - 1b
# * byte_207        - Vf Short Threshold Slow       - 1b
# * byte_208/209    - Minimum On Time               - 2b
# * byte_210/211    - Nominal Voltage               - 2b
# * byte_212        - Load Type                     - 1b
# * byte_213        - AK Power 1 Window             - 1b
# * byte_214        - AK Power 2 Window             - 1b
# * byte_215        - Dual Monitoring               - 1b
