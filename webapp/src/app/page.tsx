import Link from "next/link";

export default function Home() {
  // Datos de los modelos
  const modelos = [
    { nombre: "XGBoost", r2: 96.85, rmse: 2.71, mae: 1.15, mape: 27.35 },
    { nombre: "Random Forest", r2: 95.32, rmse: 3.31, mae: 1.35, mape: 25.52 },
    { nombre: "CatBoost", r2: 91.55, rmse: 4.45, mae: 2.31, mape: 57.44 },
    { nombre: "Ridge Regression", r2: 90.45, rmse: 4.73, mae: 0.94, mape: 18.87 },
  ];

  // Datos resumen
  const stats = [
    { label: "Precisión XGBoost", value: "96.85%", icon: "🎯" },
    { label: "Datos Analizados", value: "850,000+", icon: "📊" },
    { label: "Período", value: "2014-2025", icon: "📅" },
    { label: "Homicidios 2025", value: "8,393", icon: "⚠️" },
  ];

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-red-900 to-slate-900">
      {/* Header */}
      <nav className="fixed top-0 w-full z-50 bg-black/30 backdrop-blur-md border-b border-white/10">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🔴</span>
            <span className="font-bold text-white text-lg">Predicción Criminalidad Ecuador</span>
          </div>
          <div className="flex gap-6">
            <Link href="/" className="text-white/80 hover:text-white transition">Inicio</Link>
            <Link href="/dashboard" className="text-white/80 hover:text-white transition">Dashboard</Link>
            <Link href="/prediccion" className="text-white/80 hover:text-white transition">Predicción</Link>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-6">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 bg-red-500/20 border border-red-500/30 rounded-full px-4 py-2 mb-6">
            <span className="w-2 h-2 bg-red-500 rounded-full animate-pulse"></span>
            <span className="text-red-300 text-sm">Machine Learning • Datos Reales MDI</span>
          </div>
          
          <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
            Predicción de<br />
            <span className="bg-gradient-to-r from-red-400 to-orange-400 bg-clip-text text-transparent">
              Criminalidad en Ecuador
            </span>
          </h1>
          
          <p className="text-xl text-white/70 max-w-2xl mx-auto mb-10">
            Modelo de Machine Learning con <strong className="text-white">96.85% de precisión</strong> para 
            predecir homicidios mensuales por provincia, basado en +850,000 registros oficiales del 
            Ministerio del Interior.
          </p>

          <div className="flex justify-center gap-4 mb-16">
            <Link 
              href="/dashboard"
              className="px-8 py-4 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-lg transition-all shadow-lg shadow-red-500/25"
            >
              Ver Dashboard
            </Link>
            <Link 
              href="/prediccion"
              className="px-8 py-4 bg-white/10 hover:bg-white/20 text-white font-semibold rounded-lg transition-all border border-white/20"
            >
              Hacer Predicción
            </Link>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-4xl mx-auto">
            {stats.map((stat, i) => (
              <div key={i} className="bg-white/5 backdrop-blur border border-white/10 rounded-xl p-6">
                <div className="text-3xl mb-2">{stat.icon}</div>
                <div className="text-2xl font-bold text-white">{stat.value}</div>
                <div className="text-white/60 text-sm">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Models Comparison */}
      <section className="py-20 px-6 bg-black/30">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-3xl font-bold text-white text-center mb-4">
            Comparación de Modelos ML
          </h2>
          <p className="text-white/60 text-center mb-12">
            4 modelos entrenados con validación 80/20 temporal
          </p>

          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-white/20">
                  <th className="text-left text-white/60 py-4 px-4">#</th>
                  <th className="text-left text-white/60 py-4 px-4">Modelo</th>
                  <th className="text-center text-white/60 py-4 px-4">R²</th>
                  <th className="text-center text-white/60 py-4 px-4">RMSE</th>
                  <th className="text-center text-white/60 py-4 px-4">MAE</th>
                  <th className="text-center text-white/60 py-4 px-4">MAPE</th>
                </tr>
              </thead>
              <tbody>
                {modelos.map((modelo, i) => (
                  <tr 
                    key={i} 
                    className={`border-b border-white/10 ${i === 0 ? 'bg-red-500/10' : ''}`}
                  >
                    <td className="py-4 px-4 text-white/60">
                      {i === 0 ? '🥇' : i === 1 ? '🥈' : i === 2 ? '🥉' : i + 1}
                    </td>
                    <td className="py-4 px-4 text-white font-medium">
                      {modelo.nombre}
                      {i === 0 && <span className="ml-2 text-xs bg-red-500 text-white px-2 py-1 rounded-full">MEJOR</span>}
                    </td>
                    <td className="py-4 px-4 text-center">
                      <span className={`font-bold ${i === 0 ? 'text-green-400 text-lg' : 'text-white'}`}>
                        {modelo.r2}%
                      </span>
                    </td>
                    <td className="py-4 px-4 text-center text-white/80">{modelo.rmse}</td>
                    <td className="py-4 px-4 text-center text-white/80">{modelo.mae}</td>
                    <td className="py-4 px-4 text-center text-white/80">{modelo.mape}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

      {/* Gráfico Combinado: Homicidios + Tasa por 100k - Estilo Primicias */}
      <section className="py-16 px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-white text-center mb-4">
            📊 Evolución de la Violencia en Ecuador
          </h2>
          <p className="text-white/60 text-center mb-8">
            Homicidios intencionales y tasa por cada 100.000 habitantes
          </p>

          {/* Leyenda */}
          <div className="flex justify-center gap-8 mb-6">
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 rounded bg-amber-500"></div>
              <span className="text-white/70 text-sm">Muertes (homicidios)</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-8 h-0.5 bg-cyan-400"></div>
              <span className="text-white/70 text-sm">Tasa por 100.000 hab.</span>
            </div>
          </div>

          {/* Gráfico */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-6">
            <div className="relative h-80">
              {/* Eje Y izquierdo (Homicidios) */}
              <div className="absolute left-0 top-0 bottom-10 w-12 flex flex-col justify-between text-right pr-2">
                <span className="text-white/50 text-xs">9,000</span>
                <span className="text-white/50 text-xs">6,000</span>
                <span className="text-white/50 text-xs">3,000</span>
                <span className="text-white/50 text-xs">0</span>
              </div>

              {/* Eje Y derecho (Tasa) */}
              <div className="absolute right-0 top-0 bottom-10 w-10 flex flex-col justify-between text-left pl-2">
                <span className="text-cyan-400 text-xs">50</span>
                <span className="text-cyan-400 text-xs">35</span>
                <span className="text-cyan-400 text-xs">20</span>
                <span className="text-cyan-400 text-xs">5</span>
              </div>

              {/* Contenedor de barras y línea */}
              <div className="mx-16 h-full relative">
                {/* Datos: homicidios y tasa por 100k */}
                {(() => {
                  const datos = [
                    { año: 2014, homicidios: 1310, tasa: 8.2 },
                    { año: 2015, homicidios: 1050, tasa: 6.4 },
                    { año: 2016, homicidios: 959, tasa: 5.8 },
                    { año: 2017, homicidios: 970, tasa: 5.7 },
                    { año: 2018, homicidios: 996, tasa: 5.8 },
                    { año: 2019, homicidios: 1189, tasa: 6.8 },
                    { año: 2020, homicidios: 1372, tasa: 7.8 },
                    { año: 2021, homicidios: 2495, tasa: 14.0 },
                    { año: 2022, homicidios: 4886, tasa: 27.2 },
                    { año: 2023, homicidios: 8248, tasa: 45.2 },
                    { año: 2024, homicidios: 7063, tasa: 38.2 },
                    { año: 2025, homicidios: 8393, tasa: 47.8 },
                  ];
                  const maxHom = 9000;
                  const maxTasa = 50;

                  return (
                    <>
                      {/* Barras */}
                      <div className="absolute inset-0 flex items-end gap-1 pb-10">
                        {datos.map((d, i) => {
                          const heightPercent = (d.homicidios / maxHom) * 100;
                          return (
                            <div key={i} className="flex-1 flex flex-col items-center group relative">
                              {/* Tooltip */}
                              <div className="absolute -top-16 left-1/2 transform -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-black/90 text-white text-xs px-3 py-2 rounded z-20 whitespace-nowrap">
                                <div className="font-bold">{d.año}</div>
                                <div>Homicidios: {d.homicidios.toLocaleString()}</div>
                                <div className="text-cyan-400">Tasa: {d.tasa}</div>
                              </div>
                              
                              {/* Barra */}
                              <div className="w-full flex flex-col justify-end" style={{ height: '200px' }}>
                                <div 
                                  className="w-full bg-gradient-to-t from-amber-600 to-amber-400 rounded-t hover:brightness-110 cursor-pointer transition-all"
                                  style={{ height: `${heightPercent}%`, minHeight: '4px' }}
                                />
                              </div>
                              
                              {/* Año */}
                              <div className="text-white/60 text-xs mt-2 font-medium">{d.año}</div>
                            </div>
                          );
                        })}
                      </div>

                      {/* Línea de tasa */}
                      <svg className="absolute inset-0 w-full h-full pointer-events-none" style={{ padding: '0 0 40px 0' }}>
                        {/* Línea */}
                        <polyline
                          fill="none"
                          stroke="#22d3ee"
                          strokeWidth="3"
                          points={datos.map((d, i) => {
                            const x = 20 + (i * (100 / (datos.length - 1))) + '%';
                            const xNum = 20 + (i * (60 / (datos.length - 1)));
                            const y = 200 - (d.tasa / maxTasa) * 180;
                            return `${(i / (datos.length - 1)) * 100}%,${y}`;
                          }).join(' ')}
                          style={{ transform: 'translateX(4%)' }}
                        />
                        {/* Puntos */}
                        {datos.map((d, i) => {
                          const x = (i / (datos.length - 1)) * 92 + 4;
                          const y = 200 - (d.tasa / maxTasa) * 180;
                          return (
                            <circle
                              key={i}
                              cx={`${x}%`}
                              cy={y}
                              r="5"
                              fill="#22d3ee"
                              className="drop-shadow-lg"
                            />
                          );
                        })}
                      </svg>
                    </>
                  );
                })()}
              </div>
            </div>

            {/* Nota */}
            <p className="text-center text-white/40 text-sm mt-4">
              ⚠️ La tasa de homicidios por 100.000 habitantes pasó de <strong className="text-white/60">5.7</strong> en 2017 a <strong className="text-red-400">47.8</strong> en 2025
            </p>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-white text-center mb-12">
            Variables del Modelo
          </h2>
          
          <div className="grid md:grid-cols-3 gap-6">
            {[
              { icon: "🔫", title: "Armas Ilícitas", desc: "69,686 registros de incautación de armas ilegales" },
              { icon: "👤", title: "Personas Desaparecidas", desc: "75,000+ casos de desaparición reportados" },
              { icon: "⛓️", title: "Detenidos", desc: "556,206 registros de detenciones y aprehensiones" },
              { icon: "💊", title: "Drogas Incautadas", desc: "112,848 operativos de incautación de sustancias" },
              { icon: "📅", title: "Temporalidad", desc: "Año, mes, trimestre, lags y medias móviles" },
              { icon: "🗺️", title: "Geográfico", desc: "24 provincias + zonas no delimitadas" },
            ].map((feature, i) => (
              <div key={i} className="bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition">
                <div className="text-4xl mb-4">{feature.icon}</div>
                <h3 className="text-xl font-semibold text-white mb-2">{feature.title}</h3>
                <p className="text-white/60">{feature.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-10 px-6 border-t border-white/10">
        <div className="max-w-7xl mx-auto text-center">
          <p className="text-white/40 text-sm">
            Desarrollado por <strong className="text-white/60">Erick Reinaldo Flores Zambrano</strong> • 
            Datos: Ministerio del Interior de Ecuador (MDI) • 
            Período: 2014 - Noviembre 2025
          </p>
        </div>
      </footer>
    </main>
  );
}
