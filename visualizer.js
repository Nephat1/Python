// Canvas
const canvas = document.getElementById("nnCanvas");
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);

// Scene + Camera
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x101020);

const camera = new THREE.PerspectiveCamera(
  50,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.set(0, 0, 40);

// Neural network layout
const layers = [28 * 28, 32, 16, 10]; // MNIST-like
const spacing = 10;
const neurons = [];
const lines = [];

// Draw neurons
function createNetwork() {
  for (let l = 0; l < layers.length; l++) {
    neurons[l] = [];
    const count = layers[l];
    
    for (let n = 0; n < count; n++) {
      const geometry = new THREE.SphereGeometry(0.15, 12, 12);
      const material = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        transparent: true,
        opacity: 0.25
      });
      const sphere = new THREE.Mesh(geometry, material);

      const yOffset = (count / 2) * 0.4;

      sphere.position.x = (l - layers.length / 2) * spacing;
      sphere.position.y = (n * 0.4) - yOffset;

      scene.add(sphere);
      neurons[l].push(sphere);
    }
  }
}

// Connect neurons with lines
function connectNetwork() {
  const material = new THREE.LineBasicMaterial({
    color: 0x22ff22,
    transparent: true,
    opacity: 0.15
  });

  for (let l = 0; l < layers.length - 1; l++) {
    for (let a = 0; a < layers[l].length; a++) {
      for (let b = 0; b < layers[l + 1].length; b++) {
        const points = [];
        points.push(neurons[l][a].position);
        points.push(neurons[l + 1][b].position);

        const geo = new THREE.BufferGeometry().setFromPoints(points);
        const line = new THREE.Line(geo, material);
        scene.add(line);
        lines.push(line);
      }
    }
  }
}

// Animate
function animate() {
  requestAnimationFrame(animate);
  scene.rotation.y += 0.002;
  renderer.render(scene, camera);
}

createNetwork();
connectNetwork();
animate();