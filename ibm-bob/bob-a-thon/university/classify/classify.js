function classify(feat, dataset, k){
  if(!dataset || !dataset.length) return null;
  const ranked = dataset
    .map(s => ({ label: s.label, d: distance(feat, s.feature) }))
    .sort((a,b) => a.d - b.d);
  const votes = {};
  const kk = Math.min(k, ranked.length);
  for(let i=0;i<kk;i++) votes[ranked[i].label] = (votes[ranked[i].label] || 0) + 1;
  let best = null, bn = -1;
  for(const label in votes){ if(votes[label] > bn){ bn = votes[label]; best = label; } }
  return best;
}

