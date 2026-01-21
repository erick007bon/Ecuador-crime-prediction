import pandas as pd

df = pd.read_csv(r'C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\dataset_final_limpio.csv')

print("=" * 60)
print("=== EXPLICACIÓN DEL DATASET Y MODELO ===")
print("=" * 60)

print(f"\n📊 TOTAL FILAS: {len(df)}")
print(f"\n📅 RANGO DE AÑOS: {int(df['año'].min())} - {int(df['año'].max())}")

print("\n📋 DATOS POR AÑO:")
for año in sorted(df['año'].unique()):
    meses = df[df['año']==año]['mes'].unique()
    homicidios = df[df['año']==año]['count_homicidios'].sum()
    print(f"   {int(año)}: Meses {int(min(meses))}-{int(max(meses))}, Homicidios: {int(homicidios)}")

print("\n📋 ÚLTIMO MES DE DATOS:")
ultimo = df.sort_values(['año', 'mes']).tail(1)
print(f"   Año: {int(ultimo['año'].values[0])}, Mes: {int(ultimo['mes'].values[0])}")

print("\n" + "=" * 60)
print("=== SPLIT TRAIN/TEST ===")
print("=" * 60)

train_size = int(len(df) * 0.8)
test_size = len(df) - train_size

print(f"\n📊 Total: {len(df)} filas")
print(f"📊 Train (80%): {train_size} filas")
print(f"📊 Test (20%): {test_size} filas")

print("\n⚠️ NOTA: El split fue shuffle=False (temporal)")
print("   Esto significa que el test son los ÚLTIMOS datos")
