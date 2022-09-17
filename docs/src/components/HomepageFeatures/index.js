import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Einfache Nutzung',
    Svg: require('@site/static/img/accessibility.svg').default,
    description: (
      <>
        Durch das Zusammenspiel von sprachlicher und haptischer Interaktion mit dem System
        fällt es spielend leicht, smarte Geräte in Ihrem Haus zu steuern.
      </>
    ),
  },
  {
    title: 'Schnelle Einrichtung',
    Svg: require('@site/static/img/setup.svg').default,
    description: (
      <>
        Die Einrichtung sollte unkompliziert und schnell gehen.
        Mehr dazu unter <a href="../../../docs/intro">Installation</a>.
      </>
    ),
  },
  {
    title: 'Open Source',
    Svg: require('@site/static/img/lock_open.svg').default,
    description: (
      <>
        Durch offenen Quellcode ist es für alle möglich, das System frei zu verwenden
        und, wo nötig, an individuelle Bedürfnisse anzupassen.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
