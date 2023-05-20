<script>
	export let name;

	import { onMount } from 'svelte';
	import WaveSurfer from 'wavesurfer';

	onMount(async ()=> {
		console.log('onmount')
		const wavesurfer = WaveSurfer.create({
			container: '#waveform',
			waveColor: 'violet',
			progressColor: 'purple'
		});

		wavesurfer.load('https://wavesurfer-js.org/example/split-channels/stereo.mp3');
	});

</script>

<main>
	<h1>Acoustic Analysis {name}</h1>

	<!-- upload audio by clicking 'upload' -->
	<!-- <input type="file" id="audio" accept="audio/*" multiple on:change={handleFileInput}/> -->
	<!-- <button id="upload">Upload</button> -->
	
	
	<form action="/upload_files/" enctype="multipart/form-data" method="post">
		<input name="files" type="file" multiple>
		<input type="submit">
	</form>

	<!-- play audio -->
	<audio id="player" controls></audio>
	<!-- display audio waveform -->
	<div id="waveform">
		<canvas>
		</canvas>
	</div>

</main>

<style>
	main {
		font-family: 'Courier New', Courier, monospace;
		text-align: center;
		/* padding: 1em; */
		/* max-width: 240px; */
		/* margin: 0 auto; */
	}

	h1 {
		color: #ff00bf;
		font-weight: bold;
		font-size: 2em;
		/* font-weight: 100; */
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>