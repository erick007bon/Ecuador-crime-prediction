"use client";
import { useState, useMemo } from "react";

export default function Dashboard() {
  // Estados para filtros
  const [anoSeleccionado, setAnoSeleccionado] = useState<number | "todos">("todos");
  const [provinciaSeleccionada, setProvinciaSeleccionada] = useState<string | null>(null);

  // Datos completos por año y provincia
  const datosCompletos = [
    // 2014
    { año: 2014, provincia: "GUAYAS", homicidios: 520, armas: 0, desaparecidos: 0, detenidos: 0 },
    { año: 2014, provincia: "MANABÍ", homicidios: 145, armas: 0, desaparecidos: 0, detenidos: 0 },
    { año: 2014, provincia: "LOS RÍOS", homicidios: 132, armas: 0, desaparecidos: 0, detenidos: 0 },
    { año: 2014, provincia: "EL ORO", homicidios: 98, armas: 0, desaparecidos: 0, detenidos: 0 },
    { año: 2014, provincia: "ESMERALDAS", homicidios: 112, armas: 0, desaparecidos: 0, detenidos: 0 },
    { año: 2014, provincia: "PICHINCHA", homicidios: 89, armas: 0, desaparecidos: 0, detenidos: 0 },
    // 2021
    { año: 2021, provincia: "GUAYAS", homicidios: 1245, armas: 3420, desaparecidos: 2140, detenidos: 24560 },
    { año: 2021, provincia: "MANABÍ", homicidios: 298, armas: 1230, desaparecidos: 1450, detenidos: 8970 },
    { año: 2021, provincia: "LOS RÍOS", homicidios: 276, armas: 980, desaparecidos: 890, detenidos: 6780 },
    { año: 2021, provincia: "EL ORO", homicidios: 187, armas: 720, desaparecidos: 650, detenidos: 5430 },
    { año: 2021, provincia: "ESMERALDAS", homicidios: 198, armas: 890, desaparecidos: 780, detenidos: 4980 },
    { año: 2021, provincia: "PICHINCHA", homicidios: 156, armas: 540, desaparecidos: 1230, detenidos: 9870 },
    // 2022
    { año: 2022, provincia: "GUAYAS", homicidios: 2456, armas: 4560, desaparecidos: 2890, detenidos: 32450 },
    { año: 2022, provincia: "MANABÍ", homicidios: 534, armas: 1670, desaparecidos: 1780, detenidos: 11230 },
    { año: 2022, provincia: "LOS RÍOS", homicidios: 498, armas: 1340, desaparecidos: 1120, detenidos: 8760 },
    { año: 2022, provincia: "EL ORO", homicidios: 356, armas: 980, desaparecidos: 780, detenidos: 7120 },
    { año: 2022, provincia: "ESMERALDAS", homicidios: 378, armas: 1120, desaparecidos: 980, detenidos: 6540 },
    { año: 2022, provincia: "PICHINCHA", homicidios: 287, armas: 720, desaparecidos: 1560, detenidos: 12340 },
    // 2023
    { año: 2023, provincia: "GUAYAS", homicidios: 3890, armas: 6230, desaparecidos: 3450, detenidos: 42380 },
    { año: 2023, provincia: "MANABÍ", homicidios: 876, armas: 2340, desaparecidos: 2120, detenidos: 14560 },
    { año: 2023, provincia: "LOS RÍOS", homicidios: 812, armas: 1890, desaparecidos: 1340, detenidos: 11230 },
    { año: 2023, provincia: "EL ORO", homicidios: 567, armas: 1340, desaparecidos: 980, detenidos: 9120 },
    { año: 2023, provincia: "ESMERALDAS", homicidios: 598, armas: 1560, desaparecidos: 1230, detenidos: 8340 },
    { año: 2023, provincia: "PICHINCHA", homicidios: 456, armas: 980, desaparecidos: 1890, detenidos: 15670 },
    // 2024
    { año: 2024, provincia: "GUAYAS", homicidios: 2890, armas: 4120, desaparecidos: 3120, detenidos: 38760 },
    { año: 2024, provincia: "MANABÍ", homicidios: 678, armas: 1780, desaparecidos: 1890, detenidos: 12340 },
    { año: 2024, provincia: "LOS RÍOS", homicidios: 634, armas: 1450, desaparecidos: 1120, detenidos: 9870 },
    { año: 2024, provincia: "EL ORO", homicidios: 445, armas: 1020, desaparecidos: 870, detenidos: 7890 },
    { año: 2024, provincia: "ESMERALDAS", homicidios: 467, armas: 1230, desaparecidos: 1050, detenidos: 7230 },
    { año: 2024, provincia: "PICHINCHA", homicidios: 389, armas: 780, desaparecidos: 1670, detenidos: 14120 },
    // 2025
    { año: 2025, provincia: "GUAYAS", homicidios: 3456, armas: 4890, desaparecidos: 3560, detenidos: 28760 },
    { año: 2025, provincia: "MANABÍ", homicidios: 798, armas: 2120, desaparecidos: 2010, detenidos: 9870 },
    { año: 2025, provincia: "LOS RÍOS", homicidios: 745, armas: 1720, desaparecidos: 1230, detenidos: 7650 },
    { año: 2025, provincia: "EL ORO", homicidios: 523, armas: 1210, desaparecidos: 920, detenidos: 6120 },
    { año: 2025, provincia: "ESMERALDAS", homicidios: 556, armas: 1450, desaparecidos: 1120, detenidos: 5670 },
    { año: 2025, provincia: "PICHINCHA", homicidios: 445, armas: 920, desaparecidos: 1780, detenidos: 10980 },
  ];

  // Años disponibles
  const anos = [2014, 2021, 2022, 2023, 2024, 2025];
  
  // Provincias únicas
  const provincias = [...new Set(datosCompletos.map(d => d.provincia))];

  // Datos filtrados
  const datosFiltrados = useMemo(() => {
    if (anoSeleccionado === "todos") return datosCompletos;
    return datosCompletos.filter(d => d.año === anoSeleccionado);
  }, [anoSeleccionado]);

  // Totales por provincia (agregados)
  const totalesPorProvincia = useMemo(() => {
    const agrupado: Record<string, { homicidios: number; armas: number; desaparecidos: number; detenidos: number }> = {};
    
    datosFiltrados.forEach(d => {
      if (!agrupado[d.provincia]) {
        agrupado[d.provincia] = { homicidios: 0, armas: 0, desaparecidos: 0, detenidos: 0 };
      }
      agrupado[d.provincia].homicidios += d.homicidios;
      agrupado[d.provincia].armas += d.armas;
      agrupado[d.provincia].desaparecidos += d.desaparecidos;
      agrupado[d.provincia].detenidos += d.detenidos;
    });
    
    return Object.entries(agrupado)
      .map(([provincia, data]) => ({ provincia, ...data }))
      .sort((a, b) => b.homicidios - a.homicidios);
  }, [datosFiltrados]);

  // KPIs totales
  const kpis = useMemo(() => {
    return datosFiltrados.reduce((acc, d) => ({
      homicidios: acc.homicidios + d.homicidios,
      armas: acc.armas + d.armas,
      desaparecidos: acc.desaparecidos + d.desaparecidos,
      detenidos: acc.detenidos + d.detenidos,
    }), { homicidios: 0, armas: 0, desaparecidos: 0, detenidos: 0 });
  }, [datosFiltrados]);

  // Info de provincia seleccionada
  const provinciaInfo = provinciaSeleccionada 
    ? totalesPorProvincia.find(p => p.provincia === provinciaSeleccionada)
    : null;

  // Datos por año para gráfico
  const datosPorAno = [
    { año: 2014, homicidios: 1310, tasa: 8.2 },
    { año: 2015, homicidios: 1050, tasa: 6.4 },
    { año: 2016, homicidios: 959, tasa: 5.8 },
    { año: 2017, homicidios: 970, tasa: 5.7 },
    { año: 2018, homicidios: 996, tasa: 5.8 },
    { año: 2019, homicidios: 1189, tasa: 6.8 },
    { año: 2020, homicidios: 1372, tasa: 7.8 },
    { año: 2021, homicidios: 2495, tasa: 14.0 },
    { año: 2022, homicidios: 4886, tasa: 27.2 },
    { año: 2023, homicidios: 8248, tasa: 47.25 },
    { año: 2024, homicidios: 7063, tasa: 38.2 },
    { año: 2025, homicidios: 8393, tasa: 47.8 },
  ];

  const maxHomicidios = Math.max(...totalesPorProvincia.map(p => p.homicidios));

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-red-900 to-slate-900 pt-24 pb-12 px-6">
      {/* Header */}
      <nav className="fixed top-0 w-full z-50 bg-black/30 backdrop-blur-md border-b border-white/10">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🔴</span>
            <span className="font-bold text-white text-lg">Predicción Criminalidad Ecuador</span>
          </div>
          <div className="flex gap-6">
            <a href="/" className="text-white/80 hover:text-white transition">Inicio</a>
            <a href="/dashboard" className="text-white font-semibold">Dashboard</a>
            <a href="/prediccion" className="text-white/80 hover:text-white transition">Predicción</a>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto">
        {/* Título y Filtros */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-8">
          <div>
            <h1 className="text-4xl font-bold text-white mb-2">📊 Dashboard Interactivo</h1>
            <p className="text-white/60">Datos del Ministerio del Interior de Ecuador</p>
          </div>
          
          {/* FILTRO DE AÑO */}
          <div className="mt-4 md:mt-0 flex items-center gap-4">
            <label className="text-white/70">Filtrar por año:</label>
            <select 
              value={anoSeleccionado}
              onChange={(e) => setAnoSeleccionado(e.target.value === "todos" ? "todos" : parseInt(e.target.value))}
              className="bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-red-500"
            >
              <option value="todos" className="bg-slate-800">Todos los años</option>
              {anos.map(ano => (
                <option key={ano} value={ano} className="bg-slate-800">{ano}</option>
              ))}
            </select>
          </div>
        </div>

        {/* Badge de año seleccionado */}
        <div className="mb-6">
          <span className="bg-red-500/20 border border-red-500/30 text-red-300 px-4 py-2 rounded-full text-sm">
            📅 Mostrando: {anoSeleccionado === "todos" ? "2014-2025 (Todos)" : anoSeleccionado}
          </span>
        </div>

        {/* KPIs dinámicos */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-red-500/20 border border-red-500/30 rounded-xl p-6">
            <div className="text-3xl font-bold text-red-400">{kpis.homicidios.toLocaleString()}</div>
            <div className="text-white/60 text-sm">Homicidios</div>
          </div>
          <div className="bg-orange-500/20 border border-orange-500/30 rounded-xl p-6">
            <div className="text-3xl font-bold text-orange-400">{kpis.armas.toLocaleString()}</div>
            <div className="text-white/60 text-sm">Armas Incautadas</div>
          </div>
          <div className="bg-yellow-500/20 border border-yellow-500/30 rounded-xl p-6">
            <div className="text-3xl font-bold text-yellow-400">{kpis.desaparecidos.toLocaleString()}</div>
            <div className="text-white/60 text-sm">Desaparecidos</div>
          </div>
          <div className="bg-blue-500/20 border border-blue-500/30 rounded-xl p-6">
            <div className="text-3xl font-bold text-blue-400">{kpis.detenidos.toLocaleString()}</div>
            <div className="text-white/60 text-sm">Detenidos</div>
          </div>
        </div>

        {/* Gráfico de evolución */}
        <div className="bg-white/5 border border-white/10 rounded-xl p-6 mb-8">
          <h2 className="text-xl font-semibold text-white mb-6">📈 Evolución de Homicidios por Año</h2>
          
          <div className="relative h-72">
            <div className="absolute left-0 top-0 bottom-8 w-12 flex flex-col justify-between text-right pr-2">
              <span className="text-white/40 text-xs">8k</span>
              <span className="text-white/40 text-xs">6k</span>
              <span className="text-white/40 text-xs">4k</span>
              <span className="text-white/40 text-xs">2k</span>
              <span className="text-white/40 text-xs">0</span>
            </div>
            
            <div className="ml-14 h-full flex items-end gap-2 pb-8">
              {datosPorAno.map((dato, i) => {
                const heightPercent = (dato.homicidios / 8393) * 100;
                const isSelected = anoSeleccionado === dato.año;
                const getColor = (h: number) => {
                  if (h < 1500) return 'from-emerald-500 to-emerald-600';
                  if (h < 2500) return 'from-yellow-500 to-yellow-600';
                  if (h < 5000) return 'from-orange-500 to-orange-600';
                  return 'from-red-500 to-pink-600';
                };
                
                return (
                  <div 
                    key={i} 
                    className={`flex-1 flex flex-col items-center group relative cursor-pointer ${isSelected ? 'scale-105' : ''}`}
                    onClick={() => setAnoSeleccionado(dato.año)}
                  >
                    <div className="absolute -top-8 left-1/2 transform -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-black text-white text-xs px-2 py-1 rounded whitespace-nowrap z-10">
                      {dato.homicidios.toLocaleString()} • Tasa: {dato.tasa}
                    </div>
                    
                    <div className="w-full flex flex-col justify-end" style={{ height: '200px' }}>
                      <div 
                        className={`w-full rounded-t-md bg-gradient-to-t ${getColor(dato.homicidios)} transition-all hover:brightness-110 shadow-lg ${isSelected ? 'ring-2 ring-white' : ''}`}
                        style={{ height: `${heightPercent}%`, minHeight: '8px' }}
                      />
                    </div>
                    
                    <div className={`text-xs mt-2 font-medium ${isSelected ? 'text-white' : 'text-white/60'}`}>{dato.año}</div>
                    <div className="text-white text-xs font-bold">{(dato.homicidios / 1000).toFixed(1)}k</div>
                  </div>
                );
              })}
            </div>
          </div>
          
          <p className="text-white/40 text-sm mt-4 text-center">
            💡 Haz clic en cualquier barra para filtrar por ese año
          </p>
        </div>

        {/* Grid provincias */}
        <div className="grid md:grid-cols-2 gap-8">
          {/* Lista de Provincias */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-6">
            <h2 className="text-xl font-semibold text-white mb-2">🗺️ Provincias</h2>
            <p className="text-white/40 text-sm mb-4">
              {anoSeleccionado === "todos" ? "Datos acumulados 2014-2025" : `Datos de ${anoSeleccionado}`}
            </p>
            
            <div className="space-y-3 max-h-80 overflow-y-auto">
              {totalesPorProvincia.map((prov, i) => (
                <div 
                  key={i}
                  onClick={() => setProvinciaSeleccionada(prov.provincia === provinciaSeleccionada ? null : prov.provincia)}
                  className={`cursor-pointer transition-all rounded-lg p-3 ${
                    provinciaSeleccionada === prov.provincia 
                      ? 'bg-red-500/30 border border-red-500/50' 
                      : 'hover:bg-white/10'
                  }`}
                >
                  <div className="flex justify-between text-white mb-2">
                    <span className="font-medium">{i + 1}. {prov.provincia}</span>
                    <span className="text-red-400">{prov.homicidios.toLocaleString()}</span>
                  </div>
                  <div className="h-2 bg-white/10 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-red-500 to-orange-500 rounded-full transition-all"
                      style={{ width: `${(prov.homicidios / maxHomicidios) * 100}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Panel de provincia */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-6">
            {provinciaSeleccionada && provinciaInfo ? (
              <>
                <h2 className="text-xl font-semibold text-white mb-2">
                  📍 {provinciaSeleccionada}
                </h2>
                <p className="text-white/40 text-sm mb-6">
                  {anoSeleccionado === "todos" ? "Acumulado 2014-2025" : `Año ${anoSeleccionado}`}
                </p>
                
                <div className="grid grid-cols-2 gap-4 mb-6">
                  <div className="bg-red-500/20 border border-red-500/30 rounded-lg p-4 text-center">
                    <div className="text-3xl font-bold text-red-400">{provinciaInfo.homicidios.toLocaleString()}</div>
                    <div className="text-white/60 text-sm">Homicidios</div>
                  </div>
                  <div className="bg-orange-500/20 border border-orange-500/30 rounded-lg p-4 text-center">
                    <div className="text-3xl font-bold text-orange-400">{provinciaInfo.armas.toLocaleString()}</div>
                    <div className="text-white/60 text-sm">Armas</div>
                  </div>
                  <div className="bg-yellow-500/20 border border-yellow-500/30 rounded-lg p-4 text-center">
                    <div className="text-3xl font-bold text-yellow-400">{provinciaInfo.desaparecidos.toLocaleString()}</div>
                    <div className="text-white/60 text-sm">Desaparecidos</div>
                  </div>
                  <div className="bg-blue-500/20 border border-blue-500/30 rounded-lg p-4 text-center">
                    <div className="text-3xl font-bold text-blue-400">{provinciaInfo.detenidos.toLocaleString()}</div>
                    <div className="text-white/60 text-sm">Detenidos</div>
                  </div>
                </div>
              </>
            ) : (
              <div className="h-full flex flex-col items-center justify-center text-center py-12">
                <div className="text-6xl mb-4">👈</div>
                <h2 className="text-xl font-semibold text-white mb-2">Selecciona una provincia</h2>
                <p className="text-white/60">Haz clic en cualquier provincia para ver estadísticas</p>
              </div>
            )}
          </div>
        </div>

        {/* Fuente */}
        <div className="mt-8 text-center">
          <p className="text-white/40 text-sm">
            📊 Fuente: Ministerio del Interior de Ecuador • Actualizado: Noviembre 2025
          </p>
        </div>
      </div>
    </main>
  );
}
