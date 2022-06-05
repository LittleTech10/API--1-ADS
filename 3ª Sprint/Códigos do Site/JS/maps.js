function initMap() {
    const embraer = { lat: -23.136885031721384, lng: -45.76027680446462 };
    const gsw = { lat: -23.19099924434885, lng: -45.88835994679284};
    const pira = { lat: -23.186202506135498, lng: -45.87685801027038};
    const sonda = { lat: -23.152566467001304, lng: -45.88865880156679};
    const cartorio = { lat: -23.243312569550806, lng: -45.886471048276945};
    const labore = { lat: -23.194061943722897, lng: -45.89577313145121};
    const onset = { lat: -23.208398648257734, lng: -45.95198198912177};
    const ambev = { lat: -23.20651414394539, lng: -46.01006921627306};
    const ouro = { lat: -23.18099090175626, lng: -45.8824942179575};
    const novorh = { lat: -23.29699178439927, lng: -45.95876597377854};
    const ifJaca = { lat: -23.317392149568274, lng: -45.983692360284344};
    const it = { lat: -23.291373480106774, lng: -45.95614093083072};
    const cenaic = { lat: -23.30105045881331, lng: -45.9581291314492 };
    const micro = { lat: -23.295779273094272, lng: -45.96750287338899};
    const unopar = {lat: -23.304315855016725, lng: -45.96470943144911};
    const fatec = { lat: -23.16209511243795, lng: -45.795299502616544};
    const unifesp = { lat: -23.162661806548627, lng: -45.79315874424438};
    const senai = { lat: -23.164142717545555, lng: -45.896530731451776};
    const ifSjc = { lat: -23.18858905591971, lng: -45.85045939973092};
    const etec = { lat: -23.21187413909011, lng: -45.909824652213025};
    const senac = { lat:-23.180165975586892, lng: -45.85875974679292};
    const dita = { lat: -23.037904238802913, lng: -45.56080408542978};
    const carvalho = {lat: -23.02094313088936, lng: -45.554963859905385};
    const habib = {lat: -23.04167960094913, lng: -45.574010871935776};
    const mirasol = {lat: -23.09624429336371,  lng: -45.69112115433669};
    const logh = {lat: -23.017824407226456, lng: -45.53143444494859};
    const prefeitura = {lat: -23.096957488414635, lng: -45.7076981774606};
    const fisk = {lat: -23.101410486095116, lng: -45.7041755313886};
    const cna = {lat: -23.101188574579588, lng: -45.70807216931459};
    const johnson = {lat: -23.237092640498936, lng: -45.92341388068281};
    const ag = {lat: -23.104059357802996, lng: -45.71303475837449};
    const cia = {lat: -23.063762238932814, lng: -45.65935633138923};
    const shibata = {lat: -22.844036555535602, lng: -45.24246833139325};
    const santuario = {lat: -22.85039991253104, lng: -45.23372580255764};



    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 10,
      center: { lat: -23.093417281488644, lng: -45.67812296940821 },
    });

    new google.maps.Marker({
      position: embraer,
      map: map,
      title: 'Embraer',
    });

    new google.maps.Marker({
        position: gsw,
        map: map,
        title: 'GSW',
    });

    new google.maps.Marker({
        position: pira,
        map: map,
        title: 'Piratininga',
    });

    new google.maps.Marker({
        position: sonda,
        map: map,
        title: 'Sonda IT',
    });

    new google.maps.Marker({
        position: cartorio,
        map: map,
        title: 'Cartórios',
    });

    new google.maps.Marker({
        position: labore,
        map: map,
        title: 'Labore do Vale',
    });

    new google.maps.Marker({
        position: onset,
        map: map,
        title: 'OnSet Technology',
    });

    new google.maps.Marker({
        position: ambev,
        map: map,
        title: 'Ambev',
    });

    new google.maps.Marker({
        position: ouro,
        map: map,
        title: 'Ourho Connecta',
    });

    new google.maps.Marker({
        position: novorh,
        map: map,
        title: 'Novo TempoRH',
    });

    new google.maps.Marker({
        position: ifJaca,
        map: map,
        title: 'Instituto Jacareí',
    });

    new google.maps.Marker({
        position: cenaic,
        map: map,
        title: 'CENAIC',
    });

    new google.maps.Marker({
        position: micro,
        map: map,
        title: 'MicroCamp',
    });

    new google.maps.Marker({
        position: unopar,
        map: map,
        title: 'Unopar',
    });

    new google.maps.Marker({
        position: fatec,
        map: map,
        title: 'Fatec',
    });

    new google.maps.Marker({
        position: unifesp,
        map: map,
        title: 'UNIFESP',
    });

    new google.maps.Marker({
        position: senai,
        map: map,
        title: 'SENAI',
    });

    new google.maps.Marker({
        position: ifSjc,
        map: map,
        title: 'Instituto SJC',
    });

    new google.maps.Marker({
        position: it,
        map: map,
        title: 'Instituto de Tecnologia',
    });

    new google.maps.Marker({
        position: etec,
        map: map,
        title: 'ETEC',
    });

    new google.maps.Marker({
        position: senac,
        map: map,
        title: 'SENAC',
    });
    new google.maps.Marker({
        position: dita,
        map: map,
        title: 'DAVITA',
    });
    new google.maps.Marker({
        position: carvalho,
        map: map,
        title: 'Carvalho RH',
    });
    new google.maps.Marker({
        position: habib,
        map: map,
        title: "Habib's",
    });
    new google.maps.Marker({
        position: mirasol,
        map: map,
        title: 'Grupo Mirassol',
    });
    new google.maps.Marker({
        position: logh,
        map: map,
        title: 'Logh Logística',
    });
    new google.maps.Marker({
        position: prefeitura,
        map: map,
        title: 'Prefeitura de Caçapava',
    });
    new google.maps.Marker({
        position: fisk,
        map: map,
        title: 'FISK',
    });
    new google.maps.Marker({
        position: cna,
        map: map,
        title: 'CNA',
    });
    new google.maps.Marker({
        position: johnson,
        map: map,
        title: 'Johnson',
    });
    new google.maps.Marker({
        position: ag,
        map: map,
        title: 'AG DISTRIBUIDORA',
    });
    new google.maps.Marker({
        position: cia,
        map: map,
        title: 'Ciapellet',
    });
    new google.maps.Marker({
        position: shibata,
        map: map,
        title: 'SHIBATA Supermercados',
    });
    new google.maps.Marker({
        position: santuario,
        map: map,
        title: 'CSantuário Nacional',
    });
  }
  
  window.initMap = initMap;