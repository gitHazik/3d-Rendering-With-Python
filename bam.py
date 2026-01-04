import sys
from direct.showbase.ShowBase import ShowBase

class Converter(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
    def convert(self, input_file, output_file):
        # Load the model
        model = self.loader.loadModel(input_file)
        if model:
            model.writeBamFile(output_file)
            print(f"✓ Successfully converted {input_file} to {output_file}")
            return True
        else:
            print(f"✗ Failed to load {input_file}")
            return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_glb_to_bam.py input.glb output.bam")
        print("Example: python convert_glb_to_bam.py car.glb car.bam")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Create converter and run
    converter = Converter()
    success = converter.convert(input_file, output_file)
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)