import streamlit as st

def calculate_absolute_density(sample_weight, water_weight, sample_volume, water_volume):
    # Menghitung kerapatan absolut dalam mg/cm³
    absolute_density = ((sample_weight - water_weight) / (sample_volume - water_volume)) 
    return absolute_density

def calculate_bulk_density(sample_weight,berat_wadah, sample_volume):
    # Menghitung kerapatan curah
    bulk_density = ((sample_weight - berat_wadah) / sample_volume)
    return bulk_density

def calculate_relative_density(absolute_density, nilai_viskositas_air):
    # Menghitung kerapatan relatif
    relative_density = absolute_density / nilai_viskositas_air
    return relative_density

def main():
    st.title('Aplikasi Kalkulator Kerapatan')
    st.subheader('Kerapatan Absolut')
    st.write('Masukkan Data Untuk Menghitung Kerapatan Absolut:')
    sample_weight_abs = st.number_input ('Bobot Gelas Ukur Isi Sampel (mg):', min_value=0.0, step=0.1, format="%.4f")
    water_weight_abs = st.number_input  ('Bobot Gelas Ukur Isi Air (mg):', min_value=0.0, step=0.1, format="%.4f")
    sample_volume_abs = st.number_input ('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, step=0.1, format="%.4f")
    water_volume_abs = st.number_input ('Volume Gelas Ukur Isi Air (mL):', min_value=0.0, step=0.1, format="%.4f")

    st.subheader('Kerapatan Curah')
    st.write('Masukkan Data Untuk Menghitung Kerapatan Curah:')
    sample_weight_bulk = st.number_input ('Bobot Gelas Ukur Isi Sampel (mg):', min_value=0.0, format="%.4f", key='bulk_sample_weight')
    berat_wadah_bulk = st.number_input ('Bobot Gelas Ukur (mg):', min_value=0.0, format="%.4f", key='bulk_berat_wadah')
    sample_volume_bulk = st.number_input ('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, format="%.4f", key='bulk_sample_volume')

    st.subheader('Nilai Viskositas air')
    st.write('Masukkan Data Nilai Viskositas air:')
    nilai_viskositas_air_bulk =  st.number_input ('Nilai Viskositas air (mPa.s):', min_value=0.0, format="%.4f", key='bulk_nilai_viskositas_air')

    if st.button('Hitung Kerapatan Absolut'):
        try:
            absolute_density = calculate_absolute_density(sample_weight_abs, water_weight_abs, sample_volume_abs, water_volume_abs)
            st.subheader('Hasil Perhitungan Kerapatan Absolut:')
            st.write('Kerapatan Absolut:', absolute_density, 'mg/mL')
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

    if st.button('Hitung Kerapatan Curah'):
        try:
            bulk_density = calculate_bulk_density(sample_weight_bulk, berat_wadah_bulk, sample_volume_bulk)
            st.subheader('Hasil Perhitungan Kerapatan Curah:')
            st.write('Kerapatan Curah:', bulk_density, 'mg/mL')
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

    if st.button('Hitung Kerapatan Relatif'):
        try:
            absolute_density = calculate_absolute_density(sample_weight_abs, water_weight_abs, sample_volume_abs, water_volume_abs)
            relative_density = calculate_relative_density(absolute_density, nilai_viskositas_air_bulk)
            st.subheader('Hasil Perhitungan Kerapatan Relatif:')
            st.write('Kerapatan Relatif:', relative_density)
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

if __name__ == '__main__':
    main()
