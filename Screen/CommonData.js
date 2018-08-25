exports.getValue = (array, key) => {
  return array.filter((o) => o.key === key)[0].value
}

exports.states = [
  {key: '01', value: 'Penang'},
  {key: '02', value: 'Selangor'},
  {key: '03', value: 'Johor'},
  {key: '04', value: 'Sabah'},
  {key: '05', value: 'Sarawak'},
  {key: '06', value: 'Melaka'},
  {key: '07', value: 'Perak'},
  {key: '08', value: 'Kedah'},
  {key: '09', value: 'Pahang'},
  {key: '10', value: 'Terengganu'},
  {key: '11', value: 'Kelantan '},
  {key: '12', value: 'Negeri Sembilan'},
  {key: '13', value: 'Perlis'},
];
